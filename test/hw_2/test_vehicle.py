import unittest
from hw_2.vehicle import Vehicle
from hw_2.car import Car
from hw_2.motorcycle import Motorcycle

"""
Домашнее задание к семинару №2 JUnit:
    1. Настроить новый проект:
        a) Нужно создать новый проект, со следующей структурой классов (3 отдельных класса):

        b) Настроить тестовую среду
            (создать тестовый класс VehicleTest, пометить папку как Test sources (зеленая папка),
            импортировать необходимые для тестов библиотеки (JUnit, assertJ - все что было на семинаре))

        c) Написать следующие тесты:
            - проверка того, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
            - проверка того, объект Car создается с 4-мя колесами
            - проверка того, объект Motorcycle создается с 2-мя колесами
            - проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
            - проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
            - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта)
              машина останавливается (speed = 0)
            - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта)
              мотоцикл останавливается (speed = 0)
"""


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Lada', 'Largus', 2014)
        self.motorcycle = Motorcycle('Honda', 'CBR400R', 2023)

    def tearDown(self) -> None:
        self.car = None
        self.motorcycle = None

    def test_instance_of_vehicle(self):
        """Тест наследования объекта Car от Vehicle"""
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_wheels_car(self):
        """Тест количества колёс у объекта Car"""
        self.assertEqual(self.car.num_wheels, 4)

    def test_wheels_motorcycle(self):
        """Тест количества колёс у объекта Motorcycle"""
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_drive_car(self):
        """Тест скорости объекта Car в режиме тестового вождения """
        self.assertEqual(self.car.speed, 0)
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_drive_motorcycle(self):
        """Тест скорости объекта Motorcycle в режиме тестового вождения"""
        self.assertEqual(self.motorcycle.speed, 0)
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_park_car(self):
        """Тест скорости объекта Car в режиме парковки"""
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_park_motorcycle(self):
        """Тест скорости объекта Motorcycle в режиме парковки"""
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)
