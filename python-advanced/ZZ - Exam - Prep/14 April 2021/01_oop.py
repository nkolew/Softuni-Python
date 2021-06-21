from typing import Deque
from collections import deque


MAX_COUNT_PER_ORDER = 10


class Order:
    def __init__(self, count: int) -> None:
        self.count = count

    def __repr__(self) -> str:
        return f'{self.count}'


class Employee:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def __repr__(self) -> str:
        return f'{self.capacity}'


class PizzaShop:
    def __init__(self) -> None:
        self.__orders: Deque[Order] = deque()
        self.__employees: Deque[Employee] = deque()
        self.__pizzas_made: int = 0

    def take_orders(self) -> None:
        self.__orders = deque(Order(int(x)) for x in input().split(', '))
        self.__employees = deque(Employee(int(x)) for x in input().split(', '))

    def __validate_oders(self) -> None:
        orders_count = len(self.__orders)

        i = 0
        while True:
            if i == orders_count:
                return

            order = self.__orders.popleft()

            if 0 < order.count <= MAX_COUNT_PER_ORDER:
                self.__orders.append(order)

            i += 1

    def execute_orders(self) -> None:

        while True:
            if not self.__orders or not self.__employees:
                return

            self.__validate_oders()

            order = self.__orders.popleft()
            employee = self.__employees.pop()

            if order.count <= employee.capacity:
                self.__pizzas_made += order.count

            elif order.count > employee.capacity:
                order.count -= employee.capacity
                self.__pizzas_made += employee.capacity
                self.__orders.appendleft(order)

    def __str__(self) -> str:
        message = []
        nl = '\n'

        if not self.__orders:
            message.append('All orders are successfully completed!')
            message.append(f'Total pizzas made: {self.__pizzas_made}')
            message.append(
                f'Employees left: {", ".join(map(str, self.__employees))}')
        else:
            message.append('Not all orders are completed.')
            message.append(
                f'Orders left: {", ".join(map(str, self.__orders))}')

        return nl.join(message)


def main() -> None:
    pizzeria = PizzaShop()
    pizzeria.take_orders()
    pizzeria.execute_orders()
    print(pizzeria)


main()
