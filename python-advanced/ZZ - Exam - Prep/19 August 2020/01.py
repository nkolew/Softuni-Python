from collections import deque


class TaxiCompany:
    def __init__(self) -> None:
        self.customers = None
        self.taxis = None
        self.total_time = 0

    def populate(self):
        self.customers = deque(int(x) for x in input().split(', '))
        self.taxis = deque(int(x) for x in input().split(', '))

    def tend(self):
        while True:
            if not self.customers or not self.taxis:
                break
            current_customer = self.customers.popleft()
            current_taxi = self.taxis.pop()
            if current_taxi >= current_customer:
                self.total_time += current_customer
            else:
                self.customers.appendleft(current_customer)

    def __repr__(self) -> str:
        res = []
        if self.customers:
            res.append(f'Not all customers were driven to their destinations')
            res.append(
                f'Customers left: {", ".join(str(x) for x in self.customers)}')
        else:
            print('All customers were driven to their destinations')
            print(f'Total time: {self.total_time} minutes')
        return '\n'.join(res)


def main():
    taxi_express = TaxiCompany()
    taxi_express.populate()
    taxi_express.tend()
    print(taxi_express)


main()
