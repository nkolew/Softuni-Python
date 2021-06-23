from collections import deque


class Person:
    def __init__(self, value: int) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class CouplesMatcher:
    def __init__(self) -> None:
        self._matches = 0

    def load_data(self):
        self._males = deque(map(
            Person,
            map(int, input().split())))

        self._females = deque(map(
            Person,
            map(int, input().split())))

    def _validate_values(self, gender: str):
        persons = {
            'm': self._males,
            'f': self._females,
        }

        i = 0
        count = len(persons[gender])
        while i < count:
            person = persons[gender].popleft()
            if person.value > 0:
                persons[gender].append(person)
            i += 1

    def match_couples(self):
        self._validate_values('m')
        self._validate_values('f')

        while True:
            if not self._males or not self._females:
                return

            male = self._males.pop()
            if male.value % 25 == 0:
                self._males.pop()
                continue

            female = self._females.popleft()
            if female.value % 25 == 0:
                self._males.append(male)
                self._females.popleft()
                continue

            if male.value == female.value:
                self._matches += 1
                continue
            else:
                male.value -= 2
                if male.value > 0:
                    self._males.append(male)

    def get_stats(self) -> str:
        message = []
        nl = '\n'
        message.append(f'Matches: {self._matches}')
        message.append(
            'Males left: none' if not self._males else f'Males left: {", ".join(map(str, reversed(self._males)))}')
        message.append(
            'Females left: none' if not self._females else f'Females left: {", ".join(map(str, self._females))}')

        return nl.join(message)


def main() -> None:
    matcher = CouplesMatcher()
    matcher.load_data()
    matcher.match_couples()
    print(matcher.get_stats())


main()
