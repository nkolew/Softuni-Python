INITIAL_HEALTH = 100
INITIAL_BC = 0

health = INITIAL_HEALTH
bc = INITIAL_BC
dead = False
best_room = 0

dungeons_rooms = input().split('|')

for room in dungeons_rooms:
    best_room += 1
    command, number = room.split()
    number = int(number)
    if command == 'potion':
        if health + number > INITIAL_HEALTH:
            print(f'You healed for {INITIAL_HEALTH - health} hp.')
            health = INITIAL_HEALTH
        else:
            print(f'You healed for {number} hp.')
            health += number
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bc += number
        print(f'You found {number} bitcoins.')
    else:
        monster = command
        health -= number
        if health > 0:
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            dead = True
            break

if not dead:
    print(
        f"You've made it!\nBitcoins: {bc}\nHealth: {health}")
else:
    print(f'Best room: {best_room}')
