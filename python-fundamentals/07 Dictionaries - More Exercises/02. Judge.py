from collections import defaultdict
from typing import List, DefaultDict


class Submit:
    def __init__(self, u: str, c: str, p: int) -> None:
        self.user = u
        self.contest = c
        self.points = p

    def update(self, n: int) -> None:
        self.points = n


class Judge:
    def __init__(self) -> None:
        self.submits: List[Submit] = []

    def send_submit(self, s: Submit) -> None:
        new = True
        for submit in self.submits:
            if s.contest == submit.contest and \
                    s.user == submit.user:
                new = False
                if s.points > submit.points:
                    submit.update(s.points)
                    break
        if new:
            self.submits.append(s)

    def __get_contest_stats(self, c: str) -> str:
        participants = {
            s.user: s.points for s in self.submits if s.contest == c}
        count = len(participants)
        result = ''
        result += f'{c}: {count} participants\n'
        position = 1
        for user, points in sorted(participants.items(), key=lambda x: (-x[1], x[0])):
            result += f'{position}. {user} <::> {points}\n'
            position += 1
        return result

    def __repr__(self) -> str:
        result = ''
        contests: DefaultDict[str, int] = defaultdict(int)
        for s in self.submits:
            contests[s.contest] += 1
        for c, p in contests.items():
            c_result = self.__get_contest_stats(c)
            result += c_result

        users: DefaultDict[str, int] = defaultdict(int)
        u_result = 'Individual standings:\n'
        for s in self.submits:
            users[s.user] += s.points
        position = 1
        for u, p in sorted(users.items(), key=lambda x: (-x[1], x[0])):
            u_result += f'{position}. {u} -> {p}\n'
            position += 1
        result += u_result
        return result


j = Judge()

while True:
    data = input()
    if data == 'no more time':
        break
    username, contest, points = data.split(' -> ')
    points = int(points)
    j.send_submit(Submit(username, contest, points))

print(j)
