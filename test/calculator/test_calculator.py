import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Метод вызывается перед запуском всех тестов класса"""

    @classmethod
    def tearDownClass(cls) -> None:
        """Вызывается после прогона всех тестов класса"""

    def setUp(self) -> None:
        """Подготовка прогона теста, вызывается перед каждым тестом"""
        self.calculator = Calculator()

    def tearDown(self) -> None:
        """Вызывается после того, как тест был запущен и результат записан.
        Метод запускается даже в случае исключения (exception) в теле теста.
        """
        self.calculator = None

    def test_add(self):
        """Проверка суммирования"""
        self.assertEqual(self.calculator.add(2, 3), 5, msg='Проверка суммирования')

    def test_subtract(self):
        """Проверка вычитания"""
        self.assertEqual(self.calculator.subtract(3, 2), 1, msg='Проверка вычитания')

    def test_multiply(self):
        """Проверка умножения"""
        self.assertEqual(self.calculator.multiply(3, 2), 6, msg='Проверка умножения')

    def test_divide(self):
        """Проверка деления"""
        self.assertEqual(self.calculator.divide(4, 2), 2, msg='Проверка деления')

    def test_divide_by_zero(self):
        """Проверка деления на ноль"""
        self.assertRaises(ValueError, self.calculator.divide, 1, 0)

    @unittest.skip('Этот тест отключен')
    def test_disabled(self):
        self.fail('Этот тест не будет выполнен')

    def test_add_parametrized(self):
        """Параметризованный тест для суммирования"""
        for i in [0, 1, 2, 3]:
            with self.subTest(i=i, msg='Параметр'):
                self.assertEqual(self.calculator.add(2, i), 2 + i)

    def test_multiply_parametrized(self):
        """Параметризованный тест для умножения"""
        for i in [0, 1, 2, 3]:
            with self.subTest(i=i, msg='Параметр'):
                self.assertEqual(self.calculator.multiply(2, i), 2 * i)

    def test_assert_true(self):
        """Проверка истинного условия"""
        self.assertTrue(self.calculator.add(2, 2) == 4)

    def test_assert_false(self):
        """Проверка ложного условия"""
        self.assertFalse(self.calculator.add(2, 2) == 5)

    def test_assert_not_none(self):
        """Проверка наличия объекта"""
        self.assertIsNotNone(self.calculator)

    def test_assert_is_none(self):
        """Проверка отсутствия объекта"""
        self.calculator = None
        self.assertIsNone(self.calculator)

    def test_assert_equals(self):
        """Проверка равенства массивов -> expected == actual"""
        expected = [1, 2, 3]
        actual = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_assert_is(self):
        """Проверка равенства массивов -> expected is actual"""
        expected = [1, 2, 3]
        actual = expected
        self.assertIs(expected, actual)

    def test_discount(self):
        """Проверка расчета суммы со скидкой"""
        self.assertEqual(self.calculator.discount(1250, 10), 1125)

    def test_discount_bad_sum(self):
        """Проверка недопустимых аргументов: сумма покупки -1500"""
        self.assertRaises(ValueError, self.calculator.discount, -1500, 10)

    def test_discount_bad_discount_percent(self):
        """Проверка недопустимых аргументов: %скидки 200"""
        self.assertRaises(ValueError, self.calculator.discount, 1200, 200)

    def test_discount_bad_arguments(self):
        """Проверка недопустимых аргументов"""
        self.assertRaises(ValueError, self.calculator.discount, 0, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
