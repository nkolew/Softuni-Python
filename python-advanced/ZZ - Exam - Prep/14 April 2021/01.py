from collections import deque


MAX_ORDER_COUNT = 10

orders = deque(map(int, input().split(', ')))
employees = deque(map(int, input().split(', ')))

all_done = True
total_pizzas = 0
while True:
    if len(orders) <= 0 or len(employees) <= 0:
        break
    current_order = orders.popleft()
    if current_order > MAX_ORDER_COUNT or current_order <= 0:
        continue
    current_employee = employees.pop()
    if current_order <= current_employee:
        total_pizzas += current_order
    elif current_order > current_employee:
        current_reminder = current_order - current_employee
        while True:
            if current_reminder <= 0:
                total_pizzas += current_order
                break
            if len(employees) == 0:
                all_done = False
                orders.appendleft(current_reminder)
                break
            next_employee = employees.pop()
            current_reminder -= next_employee

if all_done:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    if employees:
        print(f'Employees: {", ".join(map(str, employees))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, orders))}')
