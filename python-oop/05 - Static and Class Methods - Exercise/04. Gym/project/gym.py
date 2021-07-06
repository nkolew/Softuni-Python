from typing import Dict, List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

        self._cusomer_by_id: Dict[int, Customer] = {}
        self._trainer_by_id: Dict[int, Trainer] = {}
        self._equipment_by_id: Dict[int, Equipment] = {}
        self._plan_by_id: Dict[int, ExercisePlan] = {}
        self._subscription_by_id: Dict[int, Subscription] = {}

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)
        self._cusomer_by_id[customer.id] = customer

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)
        self._trainer_by_id[trainer.id] = trainer

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)
        self._equipment_by_id[equipment.id] = equipment

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)
        self._plan_by_id[plan.id] = plan

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)
        self._subscription_by_id[subscription.id] = subscription

    def subscription_info(self, subscription_id: int):
        subscription = self._subscription_by_id[subscription_id]
        customer = self._cusomer_by_id[subscription.customer_id]
        trainer = self._trainer_by_id[subscription.trainer_id]
        plan = self._plan_by_id[subscription.exercise_id]
        equipment = self._equipment_by_id[plan.equipment_id]

        return '\n'.join([
            repr(subscription),
            repr(customer),
            repr(trainer),
            repr(equipment),
            repr(plan)
        ])
