from typing import List
from project.animals.animal import Bird


class Owl(Bird):
    FOOD_ALLOWED: List[str] = ['Meat']
    WEIGHT_GROWTH: float = 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    FOOD_ALLOWED: List[str] = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    WEIGHT_GROWTH: float = 0.35

    def make_sound(self):
        return 'Cluck'

