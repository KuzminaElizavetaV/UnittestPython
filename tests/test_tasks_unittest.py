import unittest
from hw_3.tasks import even_odd_number, number_in_interval


class TestTasks(unittest.TestCase):
    def test_even_number(self):
        # Проверка на четность
        self.assertTrue(even_odd_number(2))

    def test_odd_number(self):
        # Проверка на нечетность
        self.assertFalse(even_odd_number(3))

    def test_even_odd_number_bad_argument(self):
        # Проверка на число"""
        self.assertRaises(TypeError, even_odd_number, "6")

    def test_number_in_interval_less(self):
        # Проверка маленького числа
        self.assertFalse(number_in_interval(-123))

    def test_number_in_interval_true(self):
        # Проверка подходящего числа
        self.assertTrue(number_in_interval(53))

    def test_number_in_interval_more(self):
        # Проверка слишком большого числа
        self.assertFalse(number_in_interval(234))

    def test_number_in_interval_bad_argument(self):
        # Проверка на число
        self.assertRaises(TypeError, even_odd_number, "6")


if __name__ == '__main__':
    unittest.main(verbosity=2)
