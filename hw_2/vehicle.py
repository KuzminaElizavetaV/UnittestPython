from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, company: str, model: str, year_release: int) -> None:
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = 0
        self._speed = 0

    @abstractmethod
    def test_drive(self) -> None:
        ...

    @abstractmethod
    def park(self) -> None:
        ...

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def year_release(self):
        return self._year_release

    @property
    def num_wheels(self):
        return self._num_wheels

    @property
    def speed(self):
        return self._speed
