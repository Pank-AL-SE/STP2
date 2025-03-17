class Record:
    def __init__(self, p1: int, p2: int, number1: str, number2: str):
        self.p1 = p1
        self.p2 = p2
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return f"Из {self.p1}-ичной системы: {self.number1} -> В {self.p2}-ичную систему: {self.number2}"

class History:
    def __init__(self):
        self.records = []

    def add_record(self, p1: int, p2: int, number1: str, number2: str):
        """
        Добавляет запись в историю.
        """
        record = Record(p1, p2, number1, number2)
        self.records.append(record)

    def clear(self):
        """
        Очищает историю.
        """
        self.records.clear()

    def count(self) -> int:
        """
        Возвращает количество записей в истории.
        """
        return len(self.records)