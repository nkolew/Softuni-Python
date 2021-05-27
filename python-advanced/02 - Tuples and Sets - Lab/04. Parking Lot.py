from typing import List, Set


class Car:
    def __init__(self, reg_num: str) -> None:
        self.reg_num = reg_num

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.reg_num == other.reg_num

    def __hash__(self) -> int:
        return hash(self.reg_num)

    def __repr__(self) -> str:
        return self.reg_num


class Parking:
    def __init__(self) -> None:
        self.__cars: Set[Car] = set()

    def __add(self, car: Car):
        self.__cars.add(car)

    def __discard(self, car: Car):
        self.__cars.discard(car)

    def process(self, direction: str, car: Car):
        opperations = {
            'IN': self.__add,
            'OUT': self.__discard,
        }
        opperations[direction](car)

    def get_status(self) -> str:
        if self.__cars:
            nl = '\n'
            return nl.join([car.reg_num for car in self.__cars])
        else:
            return 'Parking Lot is Empty'

    def __repr__(self) -> str:
        return ', '.join([car.reg_num for car in self.__cars])


def get_n_items(n: int) -> list:
    return [input() for _ in range(n)]


def park_cars(cars: List[str]) -> Parking:
    p = Parking()
    for car_data in cars:
        direction, reg_num = car_data.split(', ')
        p.process(direction, Car(reg_num))
    return p


def main() -> None:
    n = int(input())
    cars = get_n_items(n)
    p = park_cars(cars)
    print(p.get_status())


main()
