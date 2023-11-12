from typing import List
from project.animal import Animal
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker
from project.cheetah import Cheetah


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price) -> str:
        if self.__animal_capacity <= len(self.animals):
            return 'Not enough space for animal'
        if price > self.__budget:
            return 'Not enough budget'
        self.__budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name: str):
        for obj in self.workers:
            if obj.name == worker_name:
                self.workers.remove(obj)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        workers_salary = sum([w.salary for w in self.workers])
        if workers_salary <= self.__budget:
            self.__budget -= workers_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_money_for_tend = sum([w.money_for_care for w in self.animals])
        if total_money_for_tend <= self.__budget:
            self.__budget -= total_money_for_tend
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animals_info = [f'You have {len(self.animals)} animals',
                        f'----- {len([a for a in self.animals if a.__class__ is Lion])} '
                        f'Lions:']
        lions_repr = [a.__repr__() for a in self.animals if a.__class__ is Lion]
        for a in lions_repr:
            animals_info.append(a)
        animals_info.append(f'----- {len([a for a in self.animals if a.__class__ is Tiger])} '
                            f'Tigers:')
        tigers_repr = [a.__repr__() for a in self.animals if a.__class__ is Tiger]
        for a in tigers_repr:
            animals_info.append(a)
        animals_info.append(f'----- {len([a for a in self.animals if a.__class__ is Cheetah])} '
                            f'Cheetahs:')
        cheetah_repr = [a.__repr__() for a in self.animals if a.__class__ is Cheetah]
        for a in cheetah_repr:
            animals_info.append(a)
        return '\n'.join(animals_info)

    def workers_status(self):
        workers_info = [f'You have {len(self.workers)} workers',
                        f'----- {len([w for w in self.workers if w.__class__ is Keeper])} '
                        f'Keepers:']
        keepers_repr = [w.__repr__() for w in self.workers if w.__class__ is Keeper]
        for w in keepers_repr:
            workers_info.append(w)
        workers_info.append(f'----- {len([w for w in self.workers if w.__class__ is Caretaker])} '
                            f'Caretakers:')
        caretakers_repr = [w.__repr__() for w in self.workers if w.__class__ is Caretaker]
        for w in caretakers_repr:
            workers_info.append(w)
        workers_info.append(f'----- {len([w for w in self.workers if w.__class__ is Vet])} '
                            f'Vets:')
        vets_repr = [w.__repr__() for w in self.workers if w.__class__ is Vet]
        for w in vets_repr:
            workers_info.append(w)
        return '\n'.join(workers_info)
