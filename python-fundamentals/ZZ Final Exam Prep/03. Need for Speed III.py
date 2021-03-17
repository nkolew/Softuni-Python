from typing import List

MIN_MILEAGE = 10000
MAX_MILEAGE = 100000
MAX_FUEL = 75


class Car:
    def __init__(self, name: str, mileage: int, fuel: int) -> None:
        self.name = name
        self.mileage = mileage
        self.fuel = fuel

    def __repr__(self) -> str:
        return f'{self.name} / {self.mileage} / {self.fuel}'


class CarPark:
    def __init__(self) -> None:
        self.cars: List[Car] = []

    def add_car(self, name: str, mileage: int, fuel: int) -> None:
        self.cars.append(Car(name, mileage, fuel))

    def drive(self, name: str, distance: int, fuel: int) -> None:
        for index, car in enumerate(self.cars):
            if car.name == name:
                if car.fuel < fuel:
                    print("Not enough fuel to make that ride")
                    return
                car.mileage += distance
                car.fuel -= fuel
                print(
                    f'{name} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
                if car.mileage >= MAX_MILEAGE:
                    print(f'Time to sell the {name}!')
                    self.cars.pop(index)

    def refuel(self, name: str, fuel: int) -> str:
        for car in self.cars:
            if car.name == name:
                if car.fuel + fuel > MAX_FUEL:
                    fuel = MAX_FUEL - car.fuel
                car.fuel += fuel
        return f'{name} refueled with {fuel} liters'

    def revert(self, name: str, kilometers: int) -> None:
        for car in self.cars:
            if car.name == name:
                if car.mileage - kilometers < MIN_MILEAGE:
                    kilometers = car.mileage - MIN_MILEAGE
                    car.mileage = MIN_MILEAGE
                else:
                    car.mileage -= kilometers
                    print(f'{name} mileage decreased by {kilometers} kilometers')

    def __repr__(self) -> str:
        result = []
        nl = '\n'
        for car in sorted(self.cars, key=lambda x: (-x.mileage, x.name)):
            result.append(
                f'{car.name} -> Mileage: {car.mileage} kms, Fuel in the tank: {car.fuel} lt.')
        return nl.join(result)


n = int(input())
p = CarPark()

for _ in range(n):
    name, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    p.add_car(name, mileage, fuel)

while True:
    data = input()
    if data == 'Stop':
        break
    command, *tokens = data.split(' : ')
    if command == 'Drive':
        name, mileage, fuel = tokens
        mileage = int(mileage)
        fuel = int(fuel)
        p.drive(name, mileage, fuel)
    elif command == 'Refuel':
        name, fuel = tokens
        fuel = int(fuel)
        print(p.refuel(name, fuel))
    elif command == 'Revert':
        name, kilometers = tokens
        kilometers = int(kilometers)
        p.revert(name, kilometers)

print(p)
