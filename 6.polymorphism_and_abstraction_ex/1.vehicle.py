from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AC_fc = 0.9

    def drive(self, distance: int):
        if distance <= self.fuel_quantity / (self.fuel_consumption + self.AC_fc):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_fc)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_fc = 1.6

    def drive(self, distance: int):
        if distance <= self.fuel_quantity / (self.fuel_consumption + self.AC_fc):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_fc)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95


# test code 1!
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

