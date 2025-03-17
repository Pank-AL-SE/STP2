import tkinter as tk
from tkinter import messagebox
from control import Control

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер систем счисления")
        self.control = Control()

        self.label_pin = tk.Label(root, text="Основание исходного числа (p1):")
        self.label_pin.grid(row=0, column=0, padx=10, pady=10)
        self.entry_pin = tk.Entry(root)
        self.entry_pin.insert(0, "10")
        self.entry_pin.grid(row=0, column=1, padx=10, pady=10)

        self.label_pout = tk.Label(root, text="Основание результата (p2):")
        self.label_pout.grid(row=1, column=0, padx=10, pady=10)
        self.entry_pout = tk.Entry(root)
        self.entry_pout.insert(0, "16")
        self.entry_pout.grid(row=1, column=1, padx=10, pady=10)

        self.label_input = tk.Label(root, text="Введите число:")
        self.label_input.grid(row=2, column=0, padx=10, pady=10)
        self.entry_input = tk.Entry(root)
        self.entry_input.grid(row=2, column=1, padx=10, pady=10)

        self.button_convert = tk.Button(root, text="Преобразовать", command=self.convert)
        self.button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.label_result = tk.Label(root, text="Результат:")
        self.label_result.grid(row=4, column=0, padx=10, pady=10)
        self.label_output = tk.Label(root, text="", fg="blue")
        self.label_output.grid(row=4, column=1, padx=10, pady=10)

        self.button_clear = tk.Button(root, text="Очистить", command=self.clear)
        self.button_clear.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        """
        Выполняет преобразование числа.
        """
        try:
            p1 = int(self.entry_pin.get())
            p2 = int(self.entry_pout.get())
            number = self.entry_input.get()

            self.control.pin = p1
            self.control.pout = p2

            for char in number:
                if char == '.':
                    self.control.editor.add_delim()
                elif char.isdigit() or char.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
                    if char.isdigit():
                        self.control.editor.add_digit(int(char))
                    else:
                        self.control.editor.add_digit(10 + ord(char.upper()) - ord('A'))

            result = self.control.do_command(19)
            self.label_output.config(text=result)

            self.control.editor.clear()
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def clear(self):
        """
        Очищает все поля.
        """
        self.entry_pin.delete(0, tk.END)
        self.entry_pin.insert(0, "10")
        self.entry_pout.delete(0, tk.END)
        self.entry_pout.insert(0, "16")
        self.entry_input.delete(0, tk.END)
        self.label_output.config(text="")
        self.control.editor.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()