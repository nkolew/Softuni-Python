from typing import List

from project import (Animal, Worker, Caretaker, Vet, Keeper,
                     Cheetah, Lion, Tiger)


class Zoo:
    name: str
    animals: List[Animal]
    workers: List[Worker]

    __budget: int
    __animal_capacity: int
    __workers_capacity: int

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def __has_capacity(self, attribute) -> bool:
        attributes = {
            'animals': lambda: len(self.animals) < self.__animal_capacity,
            'workers': lambda: len(self.workers) < self.__workers_capacity,
        }

        return attributes[attribute]()

    @property
    def __has_animal_capacity(self) -> bool:
        return self.__has_capacity('animals')

    @property
    def __has_workers_capacity(self) -> bool:
        return self.__has_capacity('workers')

    def __has_enough_money(self, price) -> bool:
        return self.__budget >= price

    def add_animal(self, animal: Animal, price: int) -> str:
        if not self.__has_enough_money(price):
            return 'Not enough budget'

        if isinstance(animal, Animal) \
                and self.__has_animal_capacity:

            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        return 'Not enough space for animal'

    def hire_worker(self, worker: Worker) -> str:
        if isinstance(worker, Worker) \
                and self.__has_workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return 'Not enough space for worker'

    def fire_worker(self, worker_name) -> str:
        for i, w in enumerate(self.workers):
            if w.name == worker_name:
                self.workers.pop(i)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self) -> str:
        for w in self.workers:
            if self.__budget < w.salary:
                return 'You have no budget to pay your workers. They are unhappy'
            self.__budget -= w.salary
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self) -> str:
        for a in self.animals:
            if self.__budget < a.money_for_care:
                return 'You have no budget to tend the animals. They are unhappy.'
            self.__budget -= a.money_for_care
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        message = []
        NL = '\n'

        message.append(f'You have {len(self.animals)} animals')

        lions = [a for a in self.animals if isinstance(a, Lion)]
        if lions:
            message.append(f'----- {len(lions)} Lions:')
            for l in lions:
                message.append(repr(l))

        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        if tigers:
            message.append(f'----- {len(tigers)} Tigers:')
            for t in tigers:
                message.append(repr(t))

        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]
        if cheetahs:
            message.append(f'----- {len(cheetahs)} Cheetahs:')
            for c in cheetahs:
                message.append(repr(c))

        return NL.join(message)

    def workers_status(self):
        message = []
        NL = '\n'

        message.append(f'You have {len(self.workers)} workers')

        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        if keepers:
            message.append(f'----- {len(keepers)} Keepers:')
            for k in keepers:
                message.append(repr(k))

        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        if caretakers:
            message.append(f'----- {len(caretakers)} Caretakers:')
            for c in caretakers:
                message.append(repr(c))

        vets = [w for w in self.workers if isinstance(w, Vet)]
        if vets:
            message.append(f'----- {len(caretakers)} Vets:')
            for v in vets:
                message.append(repr(v))

        return NL.join(message)
