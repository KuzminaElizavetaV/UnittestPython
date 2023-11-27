from hw_2.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self._num_wheels = 2
        self._speed = 0

    def test_drive(self):
        self._speed = 75

    def park(self):
        self._speed = 0

    def __str__(self):
        return f'{self._company} {self._model} {self._year_release} года'
