class Conver_P_10:
    @staticmethod
    def char_to_num(ch: str) -> int:
        """
        Преобразует символ в число.
        """
        if ch.isdigit():
            return int(ch)
        elif ch.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
            return 10 + ord(ch.upper()) - ord('A')
        else:
            raise ValueError(f"Недопустимый символ: {ch}")

    @staticmethod
    def dval(p_num: str, p: int) -> float:
        """
        Преобразует число из системы счисления с основанием p в десятичную.
        """
        if '.' in p_num:
            integer_part, fractional_part = p_num.split('.')
        else:
            integer_part, fractional_part = p_num, ""

        result = 0.0
        weight = 1

        # Обработка целой части
        for ch in integer_part[::-1]:
            result += Conver_P_10.char_to_num(ch) * weight
            weight *= p

        # Обработка дробной части
        weight = 1 / p
        for ch in fractional_part:
            result += Conver_P_10.char_to_num(ch) * weight
            weight /= p

        return result