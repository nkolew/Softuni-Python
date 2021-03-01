tokens = input().split('>')
explosion_strength = 0
after_explosion = []
for token in tokens:
    if token[0].isdigit():
        explosion_strength += int(token[0])
        if len(token) <= explosion_strength:
            explosion_strength -= len(token)
            token = '>'
        else:
            token = '>'+''.join(list(token[explosion_strength::]))
            explosion_strength = 0
    after_explosion.append(token)
print(''.join(after_explosion))