class TreasureChest:
    def __init__(self, items: str) -> None:
        self.items = items.split('|')

    def loot(self, l: list):
        def already_looted(loot: str):
            for item in self.items:
                if item == loot:
                    return True
            return False

        for item in l:
            if not already_looted(item):
                self.items.insert(0, item)

    def drop(self, i: int):
        def index_exists(i: int):
            if 0 <= i < len(self.items):
                return True
            return False

        if index_exists(i):
            self.items.append(self.items.pop(i))

    def steal(self, c: int):
        def get_count(c: int):
            if c > len(self.items):
                return len(self.items)
            return c

        c = get_count(c)
        stolen = []
        count = 0
        while count < c:
            stolen.append(self.items.pop())
            count += 1
        print(', '.join(reversed(stolen)))

    def __repr__(self) -> str:
        if self.items:
            gains = list(map(len, self.items))
            av_gain = sum(gains) / len(gains)
            return f'Average treasure gain: {av_gain:.2f} pirate credits.'
        return 'Failed treasure hunt.'


initial_loot = input()
chest = TreasureChest(initial_loot)

while True:
    data = input()
    if data == 'Yohoho!':
        break
    command, *token = data.split()
    if command == 'Loot':
        chest.loot(token)
    elif command == 'Drop':
        index = int(*token)
        chest.drop(index)
    elif command == 'Steal':
        count = int(*token)
        chest.steal(count)

print(chest)
