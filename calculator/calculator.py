class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> float:
        if b == 0:
            raise ValueError('Внимание, деление на ноль!')
        return a / b

    @staticmethod
    def discount(_sum: int, discount_percent: int) -> float:
        if _sum <= 0:
            raise ValueError("Сумма не должна быть равной 0 или отрицательным числом")
        if not 0 <= discount_percent <= 100:
            raise ValueError('Процент скидки должен быть больше 0 и меньше 100')
        return _sum * (1 - discount_percent / 100)
