from typing import List
from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_ALLOWED: List[str] = ['Fruit', 'Vegetable']
    WEIGHT_GROWTH: float = 0.10

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    FOOD_ALLOWED: List[str] = ['Meat']
    WEIGHT_GROWTH: float = 0.40

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    FOOD_ALLOWED: List[str] = ['Meat', 'Vegetable']
    WEIGHT_GROWTH: float = 0.30

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    FOOD_ALLOWED: List[str] = ['Meat']
    WEIGHT_GROWTH: float = 1.00

    def make_sound(self):
        return 'ROAR!!!'

