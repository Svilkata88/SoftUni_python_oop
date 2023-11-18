from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.trainer import Trainer
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscr = next(iter(s for s in self.subscriptions if s.id == subscription_id))
        customer = next(iter(c for c in self.customers if c.id == subscr.customer_id))
        trainer = next(iter(t for t in self.trainers if t.id == subscr.trainer_id))
        plan = next(iter(p for p in self.plans if p.id == subscr.exercise_id))
        equipment = next(iter(e for e in self.equipment if plan.equipment_id == e.id))
        info = [subscr, customer, trainer,equipment, plan]
        return '\n'.join([el.__repr__() for el in info])

