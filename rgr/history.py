import tkinter as tk

class CalculatorHistory:
    def __init__(self):
        self.history = []
        self.history_text = None
    
    def add_entry(self, entry):
        self.history.append(entry)
        if self.history_text:
            self.history_text.config(state='normal')
            self.history_text.insert(tk.END, entry + "\n")
            self.history_text.config(state='disabled')
            self.history_text.see(tk.END)
    
    def clear(self):
        self.history = []
        if self.history_text:
            self.history_text.config(state='normal')
            self.history_text.delete(1.0, tk.END)
            self.history_text.config(state='disabled')