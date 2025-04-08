import tkinter as tk
from tkinter import Menu

class CalculatorUI:
    def __init__(self, root, calculator):
        self.root = root
        self.calculator = calculator
        self.menu_vars = {}
        self.create_menu()
        self.create_ui()
    
    def create_menu(self):
        menubar = Menu(self.root)
        
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Копировать", command=self.calculator.copy_to_clipboard)
        edit_menu.add_command(label="Вставить", command=self.calculator.paste_from_clipboard)
        menubar.add_cascade(label="Правка", menu=edit_menu)
        
        self.view_menu = Menu(menubar, tearoff=0)
        self.menu_vars['work_mode'] = tk.StringVar(value=self.calculator.work_mode)
        
        self.view_menu.add_radiobutton(
            label="Целое",
            variable=self.menu_vars['work_mode'],
            value='integer',
            command=self.set_integer_mode
        )
        self.view_menu.add_radiobutton(
            label="Целое и дробь",
            variable=self.menu_vars['work_mode'],
            value='fraction',
            command=self.set_fraction_mode
        )
        menubar.add_cascade(label="Вид", menu=self.view_menu)
        
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="О программе", command=self.calculator.show_about)
        menubar.add_cascade(label="Справка", menu=help_menu)
        
        self.root.config(menu=menubar)

    def set_integer_mode(self):
        self.calculator.set_work_mode('integer')

    def set_fraction_mode(self):
        self.calculator.set_work_mode('fraction')
    
    def create_ui(self):
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(expand=True, fill=tk.BOTH)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        entry_frame = tk.Frame(main_frame)
        entry_frame.pack(fill=tk.X, pady=5)
        
        self.entry = tk.Entry(entry_frame, 
                             textvariable=self.calculator.entry_text, 
                             font=('Arial', 14), 
                             justify='right', 
                             bd=5,
                             relief=tk.SUNKEN)
        self.entry.pack(fill=tk.X, ipady=5)
        
        memory_frame = tk.Frame(main_frame)
        memory_frame.pack(fill=tk.X, pady=5)
        
        buttons_memory = [
            ("MC", self.calculator.memory_clear),
            ("MR", self.calculator.memory_recall),
            ("MS", self.calculator.memory_store),
            ("M+", self.calculator.memory_add)
        ]
        
        for text, cmd in buttons_memory:
            btn = tk.Button(memory_frame, 
                          text=text, 
                          width=5,
                          command=cmd)
            btn.pack(side=tk.LEFT, padx=2)
        
        self.memory_label = tk.Label(memory_frame, text=" ", width=3)
        self.memory_label.pack(side=tk.LEFT)
        
        digits_frame = tk.Frame(main_frame)
        digits_frame.pack(fill=tk.BOTH, expand=True)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(digits_frame, 
                          text=text, 
                          width=5,
                          command=lambda t=text: self.calculator.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        for i in range(4):
            digits_frame.grid_rowconfigure(i, weight=1)
            digits_frame.grid_columnconfigure(i, weight=1)
        
        extra_frame = tk.Frame(main_frame)
        extra_frame.pack(fill=tk.X, pady=5)
        
        extra_buttons = [
            ("CE", self.calculator.clear_entry),
            ("Back", self.calculator.backspace),
            ("Sqr", self.calculator.square),
            ("+/-", self.calculator.negate),
            ("1/x", self.calculator.reciprocal),
            ("Очистить историю", self.calculator.history.clear)
        ]
        
        for text, cmd in extra_buttons:
            btn = tk.Button(extra_frame, 
                          text=text,
                          command=cmd)
            btn.pack(side=tk.LEFT, padx=2)
        
        history_frame = tk.Frame(main_frame)
        history_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_text = tk.Text(history_frame, 
                                  yscrollcommand=scrollbar.set,
                                  state='disabled',
                                  wrap=tk.WORD)
        self.history_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.history_text.yview)
        self.calculator.history.history_text = self.history_text
    
    def update_memory_indicator(self, enabled):
        self.memory_label.config(text="M" if enabled else " ")