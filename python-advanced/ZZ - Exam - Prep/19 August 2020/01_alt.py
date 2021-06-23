from collections import deque


class Customer:
    def __init__(self, distance: int) -> None:
        self.distance = distance


class Taxi:
    def __init__(self, fuel: int) -> None:
        self.fuel = fuel


class TaxyCompany:
    def __init__(self) -> None:
        self.total = 0

    def load_data(self) -> None:
        self._customers = deque(map(
            Customer, map(int, input().split(', '))))
        self._taxis = deque(map(
            Taxi, map(int, input().split(', '))))

    def tend_customers(self) -> None:

        while True:
            if not self._customers or not self._taxis:
                break

            customer = self._customers.popleft()
            taxi = self._taxis.pop()

            if taxi.fuel >= customer.distance:
                self.total += customer.distance
                continue

            self._customers.appendleft(customer)

    def get_status(self) -> str:
        message = []
        nl = '\n'

        if not self._customers:
            message.append(
                'All customers were driven to their destinations')
            message.append(f'Total time: {self.total} minutes')
        else:
            message.append(
                'Not all customers were driven to their destinations')
            message.append(
                f'Customers left: {", ".join(str(c.distance) for c in  self._customers)}')

        return nl.join(message)


def main() -> None:
    taxi_express = TaxyCompany()
    taxi_express.load_data()
    taxi_express.tend_customers()
    print(taxi_express.get_status())


main()
