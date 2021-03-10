from collections import defaultdict


class Dragon:
    def __init__(self, color: str, name: str, damage: int, health: int, armor: int) -> None:
        self.id = (color, name)
        self.color = color
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __repr__(self) -> str:
        return f'{self.id} -> {self.health}, {self.damage}, {self.armor}'


class Army:
    def __init__(self) -> None:
        self.dragons = defaultdict(list)

    def add_dragon(self, d: Dragon):
        new = True
        for index, dragon in enumerate(self.dragons[d.color]):
            if d.id == dragon.id:
                new = False
                self.dragons[d.color].pop(index)
                self.dragons[d.color].insert(index, d)
        if new:
            self.dragons[d.color].append(d)

    def __repr__(self) -> str:
        result = ''
        for color, dragons in self.dragons.items():
            av_damage = sum([dragon.damage for dragon in dragons])/len(dragons)
            av_health = sum([dragon.health for dragon in dragons])/len(dragons)
            av_armor = sum([dragon.armor for dragon in dragons])/len(dragons)
            result += f'{color}::({av_damage:.2f}/{av_health:.2f}/{av_armor:.2f})\n'
            for dragon in sorted(dragons, key=lambda x: x.name):
                result += f'-{dragon.name} -> damage: {dragon.damage}, health: {dragon.health}, armor: {dragon.armor}\n'
        return result


def gen_dragon(dragon_data: list) -> Dragon:
    color: str = dragon_data[0]
    name: str = dragon_data[1]
    if dragon_data[2] == 'null':
        damage = 45
    else:
        damage = int(dragon_data[2])
    if dragon_data[3] == 'null':
        health = 250
    else:
        health = int(dragon_data[3])
    if dragon_data[4] == 'null':
        armor = 10
    else:
        armor = int(dragon_data[4])
    return Dragon(color, name, damage, health, armor)


n = int(input())

a = Army()

for _ in range(n):
    dragon_data = input().split()
    a.add_dragon(gen_dragon(dragon_data))

print(a)
