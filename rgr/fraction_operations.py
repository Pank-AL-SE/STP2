from fractions import Fraction

class FractionOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        return a / b
    
    @staticmethod
    def square(a):
        return a * a
    
    @staticmethod
    def reciprocal(a):
        if a == 0:
            raise ZeroDivisionError("Деление на ноль")
        return Fraction(1, 1) / a
    
    @staticmethod
    def negate(a):
        return -a
    
    @staticmethod
    def parse_fraction(text):
        if '/' in text:
            parts = text.split('/')
            if len(parts) != 2:
                raise ValueError("Некорректный формат дроби")
            
            numerator = parts[0]
            denominator = parts[1]
            
            if '.' in numerator or '.' in denominator:
                try:
                    num = float(numerator)
                    den = float(denominator)
                    if den == 0:
                        raise ZeroDivisionError("Деление на ноль")
                    return Fraction(num / den).limit_denominator()
                except ValueError:
                    raise ValueError("Некорректное десятичное число")
            else:
                try:
                    num = int(numerator)
                    den = int(denominator)
                    if den == 0:
                        raise ZeroDivisionError("Деление на ноль")
                    return Fraction(num, den)
                except ValueError:
                    raise ValueError("Некорректное целое число")
        elif '.' in text:
            try:
                return Fraction(text).limit_denominator()
            except ValueError:
                raise ValueError("Некорректное десятичное число")
        else:
            try:
                return Fraction(int(text), 1)
            except ValueError:
                raise ValueError("Некорректное целое число")
    
    @staticmethod
    def format_fraction(fraction, display_mode="fraction"):
        fraction = fraction.limit_denominator()
        
        if fraction.denominator == 1:
            return str(fraction.numerator)
        
        if display_mode == "integer":
            return str(fraction.numerator // fraction.denominator)
        
        return f"{fraction.numerator}/{fraction.denominator}"