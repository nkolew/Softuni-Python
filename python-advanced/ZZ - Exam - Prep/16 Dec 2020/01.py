from collections import deque


class Group:
    def __init__(self) -> None:
        self.males = None
        self.females = None
        self.matches_count = 0

    def read_males(self):
        self.males = deque(int(x) for x in input().split())

    def read_females(self):
        self.females = deque(int(x) for x in input().split())

    def match(self):

        while self.males and self.females:

            current_male = self.males.pop()
            if current_male <= 0:
                continue

            if current_male % 25 == 0:
                next_male = self.males.pop()
                continue

            current_female = self.females.popleft()
            if current_female <= 0:
                self.males.append(current_male)
                continue
            
            if current_female % 25 == 0:
                next_female = self.females.popleft()
                self.males.append(current_male)
                continue

            if current_male == current_female:
                self.matches_count += 1
                continue

            current_male -= 2
            if current_male > 0:
                self.males.append(current_male)

    def __repr__(self) -> str:
        res = []
        res.append(f'Matches: {self.matches_count}')
        if self.males:
            res.append(
                f"Males left: {', '.join(str(x) for x in reversed(self.males))}")
        else:
            res.append('Males left: none')
        if self.females:
            res.append(
                f"Females left: {', '.join(str(x) for x in self.females)}")
        else:
            res.append('Females left: none')
        return '\n'.join(res)


def main():
    group = Group()
    group.read_males()
    group.read_females()
    group.match()
    print(group)


main()
