from collections import deque
from typing import Deque, Dict

P = 'Palm'
W = 'Willow'
C = 'Crossette'
TARGET = 3


class Effect:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}'


class Power:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}'


class Firework:
    def __repr__(self) -> str:
        return f'{str(type(self)).split(".")[-1][:-2]}'


class PalmFirework(Firework):
    pass


class WillowFirework(Firework):
    pass


class CrossetteFirework(Firework):
    pass


class FireworkFactory:
    def create_firework(self, type: str) -> Firework:
        fireworks = {
            P: PalmFirework,
            W: WillowFirework,
            C: CrossetteFirework
        }

        return fireworks[type]()


class FireworksShop:
    def __init__(self) -> None:
        self.__factory: FireworkFactory = FireworkFactory()
        self.__effects: Deque[Effect] = deque()
        self.__powers: Deque[Power] = deque()
        self._fireworks: Dict[str, list] = {P: [], W: [], C: []}

    def __populate_effects(self) -> None:
        self.__effects = deque(map(
            Effect, (map(int, input().split(', ')))))

    def __populate_powers(self) -> None:
        self.__powers = deque(map(
            Power, (map(int, input().split(', ')))))

    def prepare(self) -> None:
        self.__populate_effects()
        self.__populate_powers()

    @staticmethod
    def __check_mixture_type(x: int):
        if x % 3 == 0 and x % 5 == 0:
            return C
        elif x % 3 == 0:
            return P
        elif x % 5 == 0:
            return W
        else:
            return ''

    def __validate_effects(self) -> None:
        i = 0
        effects_count = len(self.__effects)
        while i < effects_count:
            effect = self.__effects.popleft()

            if effect.value > 0:
                self.__effects.append(effect)

            i += 1

    def __validate_powers(self) -> None:
        i = 0
        powers_count = len(self.__powers)
        while i < powers_count:
            power = self.__powers.popleft()

            if power.value > 0:
                self.__powers.append(power)

            i += 1

    @property
    def __target_reached(self) -> bool:
        return all(len(fireworks) >= TARGET for fireworks in self._fireworks.values())

    def operate(self):

        self.__validate_effects()
        self.__validate_powers()

        while True:
            if not self.__effects or not self.__powers:
                return

            if self.__target_reached:
                return

            effect = self.__effects.popleft()
            power = self.__powers.pop()

            mixture_value = effect.value + power.value
            mixture_type = self.__check_mixture_type(mixture_value)

            if not mixture_type:
                self.__powers.append(power)
                effect.value -= 1
                if effect.value > 0:
                    self.__effects.append(effect)
                continue

            firework = self.__factory.create_firework(mixture_type)
            self._fireworks[mixture_type].append(firework)

    def __str__(self) -> str:
        message = []
        nl = '\n'

        if self.__target_reached:
            message.append('Congrats! You made the perfect firework show!')
        else:
            message.append('Sorry. You can\'t make the perfect firework show.')

        if self.__effects:
            message.append(
                f'Firework Effects left: {", ".join(map(str, self.__effects))}')

        if self.__powers:
            message.append(
                f'Firework Effects left: {", ".join(map(str, self.__powers))}')

        message.append(f'Palm Fireworks: {len(self._fireworks[P])}')
        message.append(f'Palm Fireworks: {len(self._fireworks[W])}')
        message.append(f'Palm Fireworks: {len(self._fireworks[C])}')

        return nl.join(message)


def main() -> None:
    shop = FireworksShop()
    shop.prepare()
    shop.operate()
    print(shop)


main()
