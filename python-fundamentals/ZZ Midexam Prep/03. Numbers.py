class Numbers:
    def __init__(self, l: list, t: int) -> None:
        self.l = l
        self.avg = 0
        self.threshold = t
        self.greater = []

    def find_avg(self):
        self.avg = sum(self.l)/len(self.l)

    def get_greater(self):
        self.greater = sorted(
            filter(lambda e: e > self.avg, self.l), reverse=True)

    def __repr__(self) -> str:
        if len(self.greater) == 0:
            return 'No'
        elif 0 < len(self.greater) <= self.threshold:
            return f'{" ".join(map(str, self.greater))}'
        else:
            return f'{" ".join(map(str, self.greater[:self.threshold]))}'


nums = list(map(int, input().split()))
THRESHOLD = 5

n = Numbers(nums, THRESHOLD)
n.find_avg()
n.get_greater()
print(n)
