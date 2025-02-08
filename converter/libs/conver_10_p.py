class Conver10P:
    
    @staticmethod
    def dval(P_num, P):
        # Проверяем наличие знака минуса
        is_negative = False
        if P_num.startswith('-'):
            is_negative = True
            P_num = P_num[1:]  # Убираем знак минус
        
        # Находим точку, отделяющую целую и дробную части
        point_index = P_num.find('.')
        
        if point_index == -1:
            return Conver10P.__convert(P_num, P, 1)
        
        integer_part = P_num[:point_index]
        fractional_part = P_num[point_index + 1:]
        
        result = Conver10P.__convert(integer_part, P, 1) + Conver10P.__convert(fractional_part, P, 1 / P)
        
        # Возвращаем результат с учетом знака
        return -result if is_negative else result
    
    @staticmethod
    def __convert(P_num, P, weight):
        result = 0
        for digit in reversed(P_num):
            result += Conver10P.__char_to_num(digit) * weight
            weight *= P
            
        return result
    
    @staticmethod
    def __char_to_num(ch):
        if '0' <= ch <= '9':
            return ord(ch) - ord('0')  # Если это цифра от 0 до 9
        elif 'a' <= ch <= 'z':  # Для букв a-z
            return ord(ch) - ord('a') + 10
        elif 'A' <= ch <= 'Z':  # Для букв A-Z
            return ord(ch) - ord('A') + 10
        else:
            raise ValueError("Некорректный символ")


# Пример использования
result = Conver10P.dval("-A5.E", 16)
print(result)  # Вывод: 165.875