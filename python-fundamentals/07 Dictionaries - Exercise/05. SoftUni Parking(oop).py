from collections import defaultdict


class User:
    def __init__(self, name: str, license: str) -> None:
        self.name = name
        self.license = license


class ParkingLot:
    def __init__(self) -> None:
        self.lot = defaultdict(list)

    def register(self, user: User):
        active = False
        for u in self.lot['active']:
            if user.name == u.name:
                active = True
                print(
                    f'ERROR: already registered with plate number {u.license}')
        if not active:
            self.lot['active'].append(user)
            print(f'{user.name} registered {user.license} successfully')

    def unregister(self, name):
        active = False
        for u in self.lot['active']:
            if name == u.name:
                print(f'{name} unregistered successfully')
                active = True
                self.lot['active'].remove(u)
                self.lot['unactive'].append(u)
        if not active:
            print(f'ERROR: user {name} not found')

    def __repr__(self) -> str:

        result = [
            f'{user.name} => {user.license}' for user in self.lot['active']
        ]
        result = '\n'.join(result)
        return result


n = int(input())
p = ParkingLot()

for _ in range(n):
    tokens = input()
    command = tokens.split()[0]
    if command == 'register':
        name, license = tokens.split()[1], tokens.split()[2]
        p.register(User(name, license))
    elif command == 'unregister':
        name = tokens.split()[1]
        p.unregister(name)

print(p)
