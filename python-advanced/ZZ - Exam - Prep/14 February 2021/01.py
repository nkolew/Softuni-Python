from collections import defaultdict, deque


ENOUGH_FIREWORKS = 3

firework_effects = deque(map(int, input().split(', ')))  # queue
explosive_powers = deque(map(int, input().split(', ')))  # stack
fireworks = defaultdict(int)


show_ready = False
while True:
    if fireworks['Palm'] >= fireworks['Willow'] >= \
            fireworks['Crossette'] >= ENOUGH_FIREWORKS:
        show_ready = True
        break
    if not firework_effects or not explosive_powers:
        break
    current_effect = firework_effects.popleft()
    if current_effect <= 0:
        continue
    current_power = explosive_powers.pop()
    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    current_sum = current_effect + current_power
    while True:
        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['Crossette'] += 1
            break
        elif current_sum % 3 == 0:
            fireworks['Palm'] += 1
            break
        elif current_sum % 5 == 0:
            fireworks['Willow'] += 1
            break
        else:
            current_effect -= 1
            if current_effect > 0:
                firework_effects.append(current_effect)
            explosive_powers.append(current_power)
        break

if show_ready:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f'Firework Effects left: {", ".join(map(str, firework_effects))}')
if explosive_powers:
    print(f'Explosive Power left: {", ".join(map(str, explosive_powers))}')
print(f"Palm Fireworks: {fireworks['Palm']}")
print(f"Willow Fireworks: {fireworks['Willow']}")
print(f"Crossette Fireworks: {fireworks['Crossette']}")
