from collections import deque


food_qty = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if orders[0] > food_qty:
        break
    food_qty -= orders.popleft()

if orders:
    print(f'Orders left: {" ".join(map(str, orders))}')
else:
    print('Orders complete')
