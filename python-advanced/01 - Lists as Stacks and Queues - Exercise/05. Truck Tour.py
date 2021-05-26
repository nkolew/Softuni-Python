from collections import deque


n = int(input())
pumps = deque()

for _ in range(n):
    fuel, dist = input().split()
    pumps.append(int(fuel)-int(dist))

for i in range(n):
    total_fuel = 0
    for pump in pumps:
        total_fuel += pump
        if total_fuel < 0:
            break
    if total_fuel >= 0:
        print(i)
        break
    else:
        pumps.append(pumps.popleft())
