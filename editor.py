class Editor:
    def __init__(self):
        self.number = ""
        self.delim = "."
        self.zero = "0"

    def add_digit(self, n: int) -> str:
        """
        Добавляет цифру в число.
        """
        if 0 <= n <= 15:
            digit = str(n) if n < 10 else chr(ord('A') + n - 10)
            self.number += digit
        else:
            raise ValueError("Цифра должна быть в диапазоне от 0 до 15.")
        return self.number

    def add_zero(self) -> str:
        """
        Добавляет ноль в число.
        """
        self.number += self.zero
        return self.number

    def add_delim(self) -> str:
        """
        Добавляет разделитель целой и дробной частей.
        """
        if self.delim not in self.number:
            self.number += self.delim
        return self.number

    def bs(self) -> str:
        """
        Удаляет последний символ числа.
        """
        if self.number:
            self.number = self.number[:-1]
        return self.number

    def clear(self) -> str:
        """
        Очищает число.
        """
        self.number = ""
        return self.number

    def do_edit(self, j: int) -> str:
        """
        Выполняет команду редактирования.
        """
        if 0 <= j <= 15:
            return self.add_digit(j)
        elif j == 16:
            return self.add_delim()
        elif j == 17:
            return self.bs()
        elif j == 18:
            return self.clear()
        else:
            raise ValueError("Недопустимый номер команды.")