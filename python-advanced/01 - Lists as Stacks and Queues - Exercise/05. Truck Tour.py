from collections import deque

n = int(input())

pumps = deque()

for _ in range(n):
    petrol_amount, distance = map(int, input().split())
    petrol_left = petrol_amount - distance
    pumps.append(petrol_left)

total_fuel = 0
for i in range(n):
    if pumps[0] >= 0:
        for pump in pumps:
            total_fuel += pump
            if total_fuel < 0:
                break
        if total_fuel >= 0:
            print(i)
            break
        else:
            pumps.append(pumps.popleft())
            total_fuel = 0
    else:
        pumps.append(pumps.popleft())
