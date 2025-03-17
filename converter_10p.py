class Conver_10_P:
    @staticmethod
    def int_to_char(d: int) -> str:
        """
        Преобразует число в символ.
        """
        if 0 <= d <= 9:
            return str(d)
        elif 10 <= d <= 15:
            return chr(ord('A') + d - 10)
        else:
            raise ValueError("Число должно быть в диапазоне от 0 до 15.")

    @staticmethod
    def int_to_p(n: int, p: int) -> str:
        """
        Преобразует целую часть числа в систему счисления с основанием p.
        """
        if n == 0:
            return "0"
        result = ""
        while n > 0:
            remainder = n % p
            result = Conver_10_P.int_to_char(remainder) + result
            n = n // p
        return result

    @staticmethod
    def flt_to_p(n: float, p: int, c: int) -> str:
        """
        Преобразует дробную часть числа в систему счисления с основанием p.
        """
        if n == 0:
            return ""
        result = ""
        for _ in range(c):
            n *= p
            digit = int(n)
            result += Conver_10_P.int_to_char(digit)
            n -= digit
        return result

    @staticmethod
    def do(n: float, p: int, c: int) -> str:
        """
        Преобразует число из десятичной системы в систему с основанием p.
        """
        negative = n < 0
        n = abs(n)

        integer_part = int(n)
        fractional_part = n - integer_part

        integer_result = Conver_10_P.int_to_p(integer_part, p)
        fractional_result = Conver_10_P.flt_to_p(fractional_part, p, c)

        result = f"{integer_result}.{fractional_result}" if fractional_result else integer_result
        return f"-{result}" if negative else result