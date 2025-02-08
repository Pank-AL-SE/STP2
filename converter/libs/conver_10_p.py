class Conver10P:
    
    @staticmethod
    def dval(P_num, P):
        # Проверка на отрицательное число
        is_negative = False
        if P_num.startswith('-'):
            is_negative = True
            P_num = P_num[1:]  # Убираем символ '-'
        
        if '.' in P_num:
            integer_part, fractional_part = P_num.split('.')
        else:
            integer_part, fractional_part = P_num, ''
        
        # Преобразование целой части
        integer_value = Conver10P.__convert(integer_part, P, 1)
        
        # Преобразование дробной части
        fractional_value = 0.0
        if fractional_part:
            fractional_weight = 1.0 / P  # Начинаем с P^{-1}
            for ch in fractional_part:
                fractional_value += Conver10P.__char_to_num(ch) * fractional_weight
                fractional_weight /= P  # Уменьшаем вес для следующего разряда
        
        # Учитываем знак числа
        result = integer_value + fractional_value
        if is_negative:
            result = -result
        
        return result
    
    @staticmethod
    def __convert(P_num, P, weight):
        result = 0.0
        for ch in P_num:
            result = result * P + Conver10P.__char_to_num(ch)
        return result / weight
    
    @staticmethod
    def __char_to_num(ch):
        if ch.isdigit():
            return int(ch)
        else:
            return ord(ch.upper()) - ord('A') + 10
print(Conver10P.dval("A5.E", 16))  # Вывод: 165.875
print(Conver10P.dval("-FF.A", 16))  # Вывод: 255.625
print(Conver10P.dval("11.1", 2))   # Вывод: 3.5