"""Сравнение средних арифметических значений списков"""
from statistics import mean


class AvgListComparison:
    """Рассчитывает средние значения двух списков и сравнивает их."""

    def __init__(self, list_1: list[int], list_2: list[int]) -> None:
        self.list_1 = list_1
        self.list_2 = list_2
        self._list_avg_1 = None
        self._list_avg_2 = None

    @property
    def list_avg_1(self) -> float | None:
        """Возвращает среднее значение первого списка"""
        if self._list_avg_1 is None and self.list_1:
            self._list_avg_1 = mean(self.list_1)
        return self._list_avg_1

    @property
    def list_avg_2(self) -> float | None:
        """Возвращает среднее значение второго списка"""
        if self._list_avg_2 is None and self.list_2:
            self._list_avg_2 = mean(self.list_2)
        return self._list_avg_2

    def compare_avg(self) -> str:
        """Сравнение среднеарифметических значений двух списков"""
        if None in (self.list_avg_1, self.list_avg_2):
            raise ValueError("Сравнение невозможно, когда один из списков пуст")
        if self.list_avg_1 > self.list_avg_2:
            return "Первый список имеет большее среднее значение"
        if self.list_avg_2 > self.list_avg_1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
