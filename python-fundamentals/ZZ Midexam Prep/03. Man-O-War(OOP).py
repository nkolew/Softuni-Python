class Ship:
    def __init__(self, status: list, max_health: int) -> None:
        self.status = status
        self.max_health = max_health
        self.sunk = False

    def index_exists(self, i: int):
        if 0 <= i < len(self.status):
            return True
        return False

    def sink(self):
        self.sunk = True

    def get_status(self):
        threshold = 0.2 * self.max_health
        need_repair = len([e for e in self.status if e < threshold])
        return f'{need_repair} sections need repair.'


class WarShip(Ship):
    def fire(self, i: int, v: int):
        if self.index_exists(i):
            self.status[i] -= v
            if self.status[i] <= 0:
                self.sink()

    def __repr__(self) -> str:
        return f'Warship status: {sum(self.status)}'


class PirateShip(Ship):
    def defend(self, i_s: int, i_e: int, v: int):
        if self.index_exists(i_s) and self.index_exists(i_e):
            for i in range(i_s, i_e+1):
                self.status[i] -= v
                if self.status[i] <= 0:
                    self.sink()
                    break

    def repair(self, i: int, v: int):
        if self.index_exists(i):
            self.status[i] += v
            if self.status[i] > self.max_health:
                self.status[i] = self.max_health

    def __repr__(self) -> str:
        return f'Pirate ship status: {sum(self.status)}'


pirateship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health = int(input())

p = PirateShip(pirateship_status, max_health)
w = WarShip(warship_status, max_health)

while True:
    data = input()
    if data == 'Retire':
        break
    command, *tokens = data.split()
    if command == 'Fire':
        index, damage = int(tokens[0]), int(tokens[1])
        w.fire(index, damage)
        if w.sunk:
            print('You won! The enemy ship has sunken.')
            break
    elif command == 'Defend':
        index_s, index_e, damage = int(
            tokens[0]), int(tokens[1]), int(tokens[2])
        p.defend(index_s, index_e, damage)
        if p.sunk:
            print('You lost! The pirate ship has sunken.')
            break
    elif command == 'Repair':
        index, health = int(tokens[0]), int(tokens[1])
        p.repair(index, health)
    elif command == 'Status':
        print(p.get_status())


if not p.sunk and not w.sunk:
    print(p)
    print(w)
