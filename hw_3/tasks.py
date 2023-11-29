# HW 3.1. Нужно покрыть тестами метод на 100%
# Метод проверяет: является ли целое число записанное в переменную n, чётным (true) либо нечётным (false).
def even_odd_number(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть числом")
    return n % 2 == 0


# HW 3.2. Нужно написать метод, который проверяет, попадает ли переданное число в интервал (25;100) и
# возвращает true, если попадает и false - если нет, покрыть тестами метод на 100%
def number_in_interval(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть числом")
    return 25 <= n <= 100


if __name__ == '__main__':
    print(even_odd_number(9))
    print(even_odd_number(26))
    print()
    print(number_in_interval(25))
    print(number_in_interval(0))



