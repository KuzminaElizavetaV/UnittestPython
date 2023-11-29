import unittest
from hw_3.tasks import even_odd_number, number_in_interval


class TestTasks(unittest.TestCase):
    def test_even_number(self):
        # �������� �� ��������
        self.assertTrue(even_odd_number(2))

    def test_odd_number(self):
        # �������� �� ����������
        self.assertFalse(even_odd_number(27))

    def test_even_odd_number_bad_argument(self):
        # �������� �� �����"""
        self.assertRaises(TypeError, even_odd_number, "6")

    def test_number_in_interval_less(self):
        # �������� ���������� �����
        self.assertFalse(number_in_interval(-25))

    def test_number_in_interval_true(self):
        # �������� ����������� �����
        self.assertTrue(number_in_interval(55))

    def test_number_in_interval_more(self):
        # �������� ������� �������� �����
        self.assertFalse(number_in_interval(158))

    def test_number_in_interval_bad_argument(self):
        # �������� �� �����
        self.assertRaises(TypeError, even_odd_number, "*")


if __name__ == '__main__':
    unittest.main(verbosity=2)
