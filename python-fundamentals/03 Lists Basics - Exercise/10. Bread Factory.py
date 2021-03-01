INITIAL_ENERGY = 100
INITIAL_COINS = 100

events = input().split('|')

total_energy = INITIAL_ENERGY
total_coins = INITIAL_COINS

bankrupt = False

for event in events:
    event_ingr, number = event.split('-')

    if event_ingr == 'rest':
        energy = int(number)

        if total_energy + energy > INITIAL_ENERGY:
            energy = INITIAL_ENERGY - total_energy
            total_energy = INITIAL_ENERGY
            print(f'You gained {energy} energy.')
            print(f'Current energy: {total_energy}.')
            continue

        total_energy += energy
        print(f'You gained {energy} energy.')
        print(f'Current energy: {total_energy}.')

    elif event_ingr == 'order':
        coins = int(number)

        if total_energy >= 30:
            total_energy -= 30
            total_coins += coins
            print(f'You earned {coins} coins.')

        else:
            total_energy += 50
            print('You had to rest!')

    else:
        ingredient = event_ingr
        coins = int(number)

        if total_coins > coins:
            total_coins -= coins
            print(f'You bought {ingredient}.')

        else:
            print(f'Closed! Cannot afford {ingredient}.')
            bankrupt = True
            break

if not bankrupt:
    print(f'Day completed!')
    print(f'Coins: {total_coins}')
    print(f'Energy: {total_energy}')