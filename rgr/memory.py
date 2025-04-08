from fractions import Fraction

class CalculatorMemory:
    def __init__(self):
        self.memory = Fraction(0, 1)
        self.memory_enabled = False
    
    def clear(self):
        self.memory = Fraction(0, 1)
        self.memory_enabled = False
    
    def store(self, value):
        self.memory = value
        self.memory_enabled = True
    
    def recall(self):
        return self.memory if self.memory_enabled else None
    
    def add(self, value):
        self.memory += value
        self.memory_enabled = True
    
    def is_enabled(self):
        return self.memory_enabled