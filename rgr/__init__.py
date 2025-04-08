from fractions import Fraction
import tkinter as tk
from tkinter import messagebox
import pyperclip
from memory import CalculatorMemory
from history import CalculatorHistory
from fraction_operations import FractionOperations

class FractionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор простых дробей")
        
        self.memory = CalculatorMemory()
        self.history = CalculatorHistory()
        self.history.history_text = None
        self.operations = FractionOperations()
        
        self.display_mode = "fraction"
        self.work_mode = "integer"
        
        self.current_value = Fraction(0, 1)
        self.entry_text = tk.StringVar()
        self.entry_text.set("0")
        self.last_operation = None
        self.last_input = None
        self.reset_input = False
        
        from ui import CalculatorUI
        self.ui = CalculatorUI(root, self)
    
    def copy_to_clipboard(self):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.entry_text.get())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось скопировать: {str(e)}")

    def paste_from_clipboard(self):
        try:
            text = self.root.clipboard_get()
            if text:
                try:
                    self.operations.parse_fraction(text)
                    self.entry_text.set(text)
                except (ValueError, ZeroDivisionError) as e:
                    messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось вставить: {str(e)}")

    def memory_clear(self):
        self.memory.clear()
        self.ui.update_memory_indicator(False)

    def memory_store(self):
        try:
            value = self.parse_input()
            self.memory.store(value)
            self.ui.update_memory_indicator(True)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def memory_recall(self):
        value = self.memory.recall()
        if value is not None:
            self.entry_text.set(self.format_fraction(value))
            self.reset_input = True

    def memory_add(self):
        try:
            value = self.parse_input()
            self.memory.add(value)
            self.ui.update_memory_indicator(True)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def parse_input(self):
        return self.operations.parse_fraction(self.entry_text.get())

    def format_fraction(self, fraction):
        return self.operations.format_fraction(fraction, self.display_mode)

    def set_work_mode(self, mode):
        self.work_mode = mode
        try:
            current_text = self.entry_text.get()
            if current_text and current_text != "0":
                value = self.parse_input()
                if mode == "integer":
                    value = Fraction(int(value), 1)
                self.entry_text.set(self.format_fraction(value))
        except ValueError:
            self.entry_text.set("0")
        
        if hasattr(self.ui, 'menu_vars'):
            self.ui.menu_vars['work_mode'].set(mode)

    def on_button_click(self, button_text):
        if button_text.isdigit():
            self.add_digit(button_text)
        elif button_text == '.':
            self.add_decimal_point()
        elif button_text in '+-*/':
            self.set_operation(button_text)
        elif button_text == '=':
            if self.last_operation and self.reset_input and self.last_input is not None:
                self.repeat_calculation()
            else:
                self.calculate()

    def add_digit(self, digit):
        if self.reset_input:
            self.entry_text.set("0")
            self.reset_input = False
        
        current = self.entry_text.get()
        if current == "0":
            self.entry_text.set(digit)
        else:
            self.entry_text.set(current + digit)

    def add_decimal_point(self):
        if self.work_mode == "integer":
            return
            
        current = self.entry_text.get()
        if '/' not in current and '.' not in current:
            self.entry_text.set(current + '.')

    def clear_entry(self):
        self.entry_text.set("0")

    def backspace(self):
        current = self.entry_text.get()
        if len(current) > 1:
            self.entry_text.set(current[:-1])
        else:
            self.entry_text.set("0")

    def set_operation(self, op):
        try:
            value = self.parse_input()
            self.current_value = value
            self.last_input = value
            if op != '=':
                self.last_operation = op
            self.reset_input = True
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def calculate(self):
        try:
            new_value = self.parse_input()
            self.last_input = new_value
            
            if self.last_operation:
                if self.last_operation == '+':
                    result = self.operations.add(self.current_value, new_value)
                elif self.last_operation == '-':
                    result = self.operations.subtract(self.current_value, new_value)
                elif self.last_operation == '*':
                    result = self.operations.multiply(self.current_value, new_value)
                elif self.last_operation == '/':
                    result = self.operations.divide(self.current_value, new_value)
                
                history_entry = f"{self.format_fraction(self.current_value)} {self.last_operation} {self.format_fraction(new_value)} = {self.format_fraction(result)}"
                self.history.add_entry(history_entry)
                
                self.current_value = result
                self.entry_text.set(self.format_fraction(result))
                self.reset_input = True
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", str(e))
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def repeat_calculation(self):
        if self.last_operation and self.last_input is not None:
            try:
                if self.last_operation == '+':
                    result = self.operations.add(self.current_value, self.last_input)
                elif self.last_operation == '-':
                    result = self.operations.subtract(self.current_value, self.last_input)
                elif self.last_operation == '*':
                    result = self.operations.multiply(self.current_value, self.last_input)
                elif self.last_operation == '/':
                    result = self.operations.divide(self.current_value, self.last_input)
                
                history_entry = f"{self.format_fraction(self.current_value)} {self.last_operation} {self.format_fraction(self.last_input)} = {self.format_fraction(result)}"
                self.history.add_entry(history_entry)
                
                self.current_value = result
                self.entry_text.set(self.format_fraction(result))
                self.reset_input = True
            except ZeroDivisionError as e:
                messagebox.showerror("Ошибка", str(e))

    def square(self):
        try:
            value = self.parse_input()
            result = self.operations.square(value)
            self.history.add_entry(f"Sqr({self.format_fraction(value)}) = {self.format_fraction(result)}")
            self.entry_text.set(self.format_fraction(result))
            self.reset_input = True
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def reciprocal(self):
        try:
            value = self.parse_input()
            result = self.operations.reciprocal(value)
            self.entry_text.set(self.format_fraction(result))
            self.reset_input = True
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", str(e))
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def negate(self):
        try:
            value = self.parse_input()
            result = self.operations.negate(value)
            self.entry_text.set(self.format_fraction(result))
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def show_about(self):
        about_text = """Калькулятор простых дробей
Версия 1.0
        
Разработчик: Pank Aleksandr
        
Функции:
- Работа с простыми дробями
- Операции: +, -, *, /
- Память (MC, MR, MS, M+)
- История вычислений
- Поддержка буфера обмена"""
        messagebox.showinfo("О программе", about_text)