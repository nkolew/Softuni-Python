from collections import deque


class MilkShakeFactory:
    def __init__(self) -> None:
        self.milkshakes = 0

    def load_data(self):
        self.chocolates = deque(map(int, input().split(', ')))
        self.milk = deque(map(int, input().split(', ')))

    @property
    def _has_enough_milkshakes(self):
        return self.milkshakes >= 5

    def mix_em_up(self):
        while True:
            if self._has_enough_milkshakes:
                break
            
            if not self.chocolates or not self.milk:
                break

            last_chocolate = self.chocolates.pop()
            first_milk = self.milk.popleft()

            if last_chocolate <= 0 and first_milk <= 0:
                continue

            if last_chocolate <= 0:
                self.milk.appendleft(first_milk)
                continue

            if first_milk <= 0:
                self.chocolates.append(last_chocolate)
                continue

            if last_chocolate == first_milk:
                self.milkshakes += 1
                continue

            else:
                self.milk.append(first_milk)
                last_chocolate -= 5
                self.chocolates.append(last_chocolate)
                continue

    def __repr__(self) -> str:
        message = []
        nl = '\n'

        if self._has_enough_milkshakes:
            message.append(
                'Great! You made all the chocolate milkshakes needed!')
        else:
            message.append('Not enough milkshakes.')

        message.append(
            'Chocolate: empty' if not self.chocolates else f'Chocolate: {", ".join(map(str, self.chocolates))}')
        message.append(
            'Milk: empty' if not self.milk else f'Milk: {", ".join(map(str, self.milk))}')

        return nl.join(message)


def main():
    ms_factory = MilkShakeFactory()
    ms_factory.load_data()
    ms_factory.mix_em_up()
    print(ms_factory)


main()
