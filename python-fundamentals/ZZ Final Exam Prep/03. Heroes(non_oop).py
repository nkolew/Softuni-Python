MAX_HP = 100
MAX_MP = 200


def cast_spell(d: dict, name: str, mp: int, spell: str) -> dict:
    if d[name]['mp'] >= mp:
        d[name]['mp'] -= mp
        print(
            f'{name} has successfully cast {spell} and now has {d[name]["mp"]} MP!')
    else:
        print(f'{name} does not have enough MP to cast {spell}!')
    return d


def take_damage(d: dict, name: str, damage: int, attacker: str) -> dict:
    d[name]['hp'] -= damage
    if d[name]['hp'] > 0:
        print(
            f'{name} was hit for {damage} HP by {attacker} and now has {d[name]["hp"]} HP left!')
    else:
        d.pop(name)
        print(f'{name} has been killed by {attacker}!')
    return d


def recharge(d: dict, name: str, amount: int) -> dict:
    amount = (amount if amount + d[name]['mp'] < MAX_MP
              else MAX_MP - d[name]['mp'])
    d[name]['mp'] += amount
    print(f'{name} recharged for {amount} MP!')
    return d


def heal(d: dict, name: str, amount: int) -> dict:
    amount = (amount if amount + d[name]['hp'] < MAX_HP
              else MAX_HP - d[name]['mp'])
    d[name]['hp'] += amount
    print(f'{name} healed for {amount} HP!"')
    return d


heroes = {}

n = int(input())

for _ in range(n):
    name, hp, mp = input().split()
    hp = int(hp) if int(hp) < MAX_HP else MAX_HP
    mp = int(mp) if int(mp) < MAX_MP else MAX_MP
    heroes[name] = {'hp': hp, 'mp': mp}

while True:
    data = input()
    if data == 'End':
        break
    command, *tokens = data.split(' - ')
    if command == 'CastSpell':
        name, mp_needed, spell = tokens
        mp_needed = int(mp_needed)
        heroes = cast_spell(heroes, name, mp_needed, spell)
    elif command == 'TakeDamage':
        name, damage, attacker = tokens
        damage = int(damage)
        heroes = take_damage(heroes, name, damage, attacker)
    elif command == 'Recharge':
        name, amount = tokens
        amount = int(amount)
        heroes = recharge(heroes, name, amount)
    elif command == 'Heal':
        name, amount = tokens
        amount = int(amount)
        heroes = heal(heroes, name, amount)

for name, stats in sorted(heroes.items(), key=lambda x: (-x[1]['hp'], x[0])):
    print(f'{name}')
    print(f' HP: {stats["hp"]}')
    print(f' MP: {stats["mp"]}')
