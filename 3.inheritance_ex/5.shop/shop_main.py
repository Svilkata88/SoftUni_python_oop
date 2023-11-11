from project.food import Food
from project.drink import Drink
from project.product_repository import ProductRepository

food = Food('apple')
drink = Drink('water')
repo = ProductRepository()
repo.add(food)
repo.add(drink)
repo.find("apple").decrease(5)

