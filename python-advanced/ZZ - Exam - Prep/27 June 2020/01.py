from collections import deque


class BombPouch:
    def __init__(self) -> None:
        self.bombs = None
        self.bombs_ready = False
        self.effects = None
        self.casings = None

    def populate(self):
        self.effects = deque(map(int, input().split(', ')))
        self.casings = deque(map(int, input().split(', ')))

    def create_bombs(self):
        recipes = {
            'Datura Bombs': 40,
            'Cherry Bombs': 60,
            'Smoke Decoy Bombs': 120,
        }

        self.bombs = {bomb: 0 for bomb in recipes}

        while True:
            if not self.effects or not self.casings:
                break
            if all(x >= 3 for x in self.bombs.values()):
                self.bombs_ready = True
                break

            current_effect = self.effects.popleft()
            current_casing = self.casings.pop()

            current_price = current_effect + current_casing
            for bomb, price in recipes.items():
                if current_price == price:
                    self.bombs[bomb] += 1
                    break

            else:
                current_casing -= 5
                self.effects.appendleft(current_effect)
                self.casings.append(current_casing)
                

    def __repr__(self) -> str:
        res = []
        nl = '\n'
        if self.bombs_ready:
            res.append('Bene! You have successfully filled the bomb pouch!')
        else:
            res.append(
                "You don't have enough materials to fill the bomb pouch.")
        if self.effects:
            res.append(f'Bomb Effects: {", ".join(map(str, self.effects))}')
        else:
            res.append('Bomb Effects: empty')
        if self.casings:
            res.append(f'Bomb Casings: {", ".join(map(str, self.casings))}')
        else:
            res.append('Bomb Casings: empty')
        for bomb, count in sorted(self.bombs.items()):
            res.append(f'{bomb}: {count}')

        return nl.join(res)


def main():
    pouch = BombPouch()
    pouch.populate()
    pouch.create_bombs()
    print(pouch)


main()
