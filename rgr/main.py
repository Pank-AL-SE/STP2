import tkinter as tk
from calculator import FractionCalculator

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600")
    app = FractionCalculator(root)
    root.mainloop()