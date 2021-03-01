energy = int(input())
failed = False
battles_won = 0

while True:
    tokens = input()
    if tokens == 'End of battle':
        break
    distance = int(tokens)
    if energy >= distance:
        energy -= distance
        battles_won += 1
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(
            f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        failed = True
        break

if not failed:
    print(f'Won battles: {battles_won}. Energy left: {energy}')
