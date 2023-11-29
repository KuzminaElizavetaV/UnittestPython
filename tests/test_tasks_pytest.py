import pytest
from contextlib import nullcontext as does_not_raise
from hw_3.tasks import even_odd_number, number_in_interval
"""Проверка"""


# Параметризованный тест проверка на четность-нечетность + ошибки
@pytest.mark.parametrize(
    "number, result, expectation",
    [
        (9, False, does_not_raise()),
        (8, True, does_not_raise()),
        (145, False, does_not_raise()),
        (214, True, does_not_raise()),
        (1, False, does_not_raise()),
        (1500, True, does_not_raise()),
        (0, True, does_not_raise()),
        ("25", True, pytest.raises(TypeError)),
        ("/", True, pytest.raises(TypeError)),
        (200, True, does_not_raise()),

    ]
)
def test_even_odd_number(number, result, expectation):
    with expectation:
        assert even_odd_number(number) == result


# Параметризованный тест проверки чисел на принадлежность к интервалу (25-100) + ошибки
@pytest.mark.parametrize(
    "number, result, expectation",
    [
        (-1, False, does_not_raise()),
        (25, True, does_not_raise()),
        (0, False, does_not_raise()),
        (48, True, does_not_raise()),
        (1, False, does_not_raise()),
        (100, True, does_not_raise()),
        (82, True, does_not_raise()),
        ("25", True, pytest.raises(TypeError)),
    ]
)
def test_number_in_interval(number, result, expectation):
    with expectation:
        assert number_in_interval(number) == result


if __name__ == '__main__':
    pytest.main()
