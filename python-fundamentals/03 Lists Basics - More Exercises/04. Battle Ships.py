n = int(input())

field = []
attacks = []
ships_destroyed = 0

for i in range(n):
    field.append([int(num) for num in input().split()])

for attack in input().split():
    x, y = attack.split('-')
    x = int(x)
    y = int(y)

    if not field[x][y]:
        continue

    field[x][y] -= 1

    if field[x][y] == 0:
        ships_destroyed += 1

print(ships_destroyed)
