class ADTConver10P:

    @staticmethod
    def _int_to_Char(d):

        if 0 <= d <= 9:
            return str(d)
        elif 10 <= d <= 35:
            return chr(ord('A') + d - 10)
        else:
            raise ValueError("Недопустимое значение для преобразования в символ системы счисления.")


    @staticmethod
    def _int_to_P(n, p):
        """Преобразует целое число в строку в системе счисления с основанием p."""
        if n == 0:
            return "0"
        result = ""
        negative = False
        if n < 0:
            negative = True
            n = -n
        while n > 0:
            remainder = n % p
            result = ADTConver10P._int_to_Char(remainder) + result
            n = n // p
        if negative:
            result = "-" + result
        return result


    @staticmethod
    def _flt_to_P(n, p, c):
        """Преобразует дробную часть числа в строку в системе счисления с основанием p."""
        result = ""
        for _ in range(c):
            n *= p
            digit = int(n)
            result += ADTConver10P._int_to_Char(digit)
            n -= digit
        return result


    @staticmethod
    def do(n: float, p: int, c: int) -> str:
        """Преобразует десятичное действительное число n в систему счисления с основанием p и точностью c."""
        try:
            n = float(n)
        except:
            raise ValueError(f'Can not convert to float or int n={n}')
        try:
            p = int(p)
            c = int(c)
        except:
            raise ValueError(f'Can not convert to int c={c} or p={p}')

        if p < 2 or p > 16:
            raise ValueError("Основание системы счисления должно быть между 2 и 16.")
        # Разделяем число на целую и дробную части
        integer_part = int(n)
        fractional_part = abs(n) - abs(integer_part)
        
        # Преобразуем целую часть
        integer_result = ADTConver10P._int_to_P(integer_part, p)
        
        # Преобразуем дробную часть
        fractional_result = ADTConver10P._flt_to_P(fractional_part, p, c)
        
        # Собираем результат
        if fractional_result:
            return f"{integer_result}.{fractional_result}"
        else:
            return integer_result

# Пример использования:
print(ADTConver10P.do(-17.875, 16, 3))  # Вывод: "-11.E"
