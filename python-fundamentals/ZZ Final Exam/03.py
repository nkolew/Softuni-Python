import re


def add(d: dict, p: str, h: int, e: int) -> dict:
    if p not in d:
        d[p] = {'health': h, 'energy': e}
    else:
        d[p]['health'] += h
    return d


def attack(d: dict, attacker: str, defender: str, damage: int) -> dict:
    if attacker in d and defender in d:
        d[defender]['health'] -= damage
        if d[defender]['health'] <= 0:
            d.pop(defender)
            print(f'{defender} was disqualified!')
        d[attacker]['energy'] -= 1
        if d[attacker]['energy'] <= 0:
            d.pop(attacker)
            print(f'{attacker} was disqualified!')
    return d


def delete(d: dict, p: str) -> dict:
    if p == 'All':
        d.clear()
    else:
        d.pop(p)
    return d


battle = {}

while True:
    data = input()
    if data == 'Results':
        break
    command, *tokens = data.split(':')
    if command == 'Add':
        person, health, energy = tokens
        health, energy = int(health), int(energy)
        battle = add(battle, person, health, energy)
    elif command == 'Attack':
        attacker, defender, damage = tokens
        damage = int(damage)
        battle = attack(battle, attacker, defender, damage)
    elif command == 'Delete':
        battle = delete(battle, *tokens)

print(f'People count: {len(battle)}')
for person, stats in sorted(battle.items(), key=lambda x: (-x[1]['health'], x[0])):
    print(f'{person} - {stats["health"]} - {stats["energy"]}')
