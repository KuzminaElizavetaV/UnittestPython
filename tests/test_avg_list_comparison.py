import pytest
from hw_6.avg_list_comparison import AvgListComparison


@pytest.fixture
def small_list():
    return [1, 0, 8, 3, 10]


@pytest.fixture
def big_list():
    return [11, 82, 50, 35]


@pytest.fixture
def simple_list():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def comparison_instance_second_gt(small_list, big_list):
    return AvgListComparison(small_list, big_list)


@pytest.fixture
def comparison_instance_first_gt(small_list, big_list):
    return AvgListComparison(big_list, small_list)


@pytest.fixture
def comparison_instance_eq(simple_list):
    return AvgListComparison(simple_list, list(reversed(simple_list)))


@pytest.fixture
def comparison_instance_empty(simple_list, empty_list):
    return AvgListComparison(simple_list, empty_list)


def test_list_avg_1(comparison_instance_second_gt):
    """Проверка среднеарифметического значения первого списка"""
    assert comparison_instance_second_gt.list_avg_1 == 4.4, "Среднее значение первого списка должно быть равно 4.4"


def test_list_avg_2(comparison_instance_second_gt):
    """Проверка среднеарифметического значения второго списка"""
    assert comparison_instance_second_gt.list_avg_2 == 44.5, "Среднее значение второго списка должно быть равно 44.5"


def test_compare_avg_second_gt_first(comparison_instance_second_gt):
    """Проверка сравнения двух списков, когда среднее значение второго списка больше"""
    assert comparison_instance_second_gt.compare_avg() == "Второй список имеет большее среднее значение"


def test_compare_avg_first_gt_second(comparison_instance_first_gt):
    """Проверка сравнения двух списков, когда среднее значение первого списка больше"""
    assert comparison_instance_first_gt.compare_avg() == "Первый список имеет большее среднее значение"


def test_compare_avg_first_eq_second(comparison_instance_eq):
    """Проверка сравнения двух списков, когда средние значения списков равны"""
    assert comparison_instance_eq.compare_avg() == "Средние значения равны"


def test_compare_avg_with_empty_list(comparison_instance_empty):
    """Проверка сравнения двух списков, когда один из списков пуст"""
    with pytest.raises(ValueError):
        comparison_instance_empty.compare_avg()


if __name__ == '__main__':
    pytest.main(['-v'])
