from hw_2.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self._num_wheels = 4
        self._speed = 0

    def test_drive(self):
        self._speed = 60

    def park(self):
        self._speed = 0

    def __str__(self):
        return f'This car is a {self._year_release} year {self._company} {self._model}'