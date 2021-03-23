MIN_MILEAGE = 10_000
MAX_MILEAGE = 100_000
TANK_CAPACITY = 75


def drive(d: dict, name: str, distance: int, fuel: int) -> dict:
    if d[name]['fuel'] < fuel:
        print('Not enough fuel to make that ride')
        return d
    d[name]['fuel'] -= fuel
    d[name]['mileage'] += distance
    print(f'{name} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
    if d[name]['mileage'] > MAX_MILEAGE:
        d.pop(name)
        print(f'Time to sell the {name}!')
    return d


def refuel(d: dict, name: str, fuel: int) -> dict:
    fuel = (fuel if d[name]['fuel'] + fuel < TANK_CAPACITY
            else TANK_CAPACITY - d[name]['fuel'])
    d[name]['fuel'] += fuel
    print(f'{name} refueled with {fuel} liters')
    return d


def revert(d: dict, name: str, kilometers: int) -> dict:
    d[name]['mileage'] -= kilometers
    if d[name]['mileage'] < MIN_MILEAGE:
        d[name]['mileage'] = MIN_MILEAGE
        return d
    print(f'{name} mileage decreased by {kilometers} kilometers')
    return d


cars = {}

n = int(input())

for _ in range(n):
    name, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[name] = {'mileage': mileage, 'fuel': fuel}

while True:
    data = input()
    if data == 'Stop':
        break
    command, *tokens = data.split(' : ')
    if command == 'Drive':
        name, kilometers, fuel = tokens
        kilometers = int(kilometers)
        fuel = int(fuel)
        cars = drive(cars, name, kilometers, fuel)
    if command == 'Refuel':
        name, fuel = tokens
        fuel = int(fuel)
        cars = refuel(cars, name, fuel)
    if command == 'Revert':
        name, kilometers = tokens
        kilometers = int(kilometers)
        cars = revert(cars, name, kilometers)

for name, stats in sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0])):
    print(
        f'{name} -> Mileage: {stats["mileage"]} kms, Fuel in the tank: {stats["fuel"]} lt.')
