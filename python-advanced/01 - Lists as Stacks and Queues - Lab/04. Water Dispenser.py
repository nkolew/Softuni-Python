from collections import deque

people = deque()
liters_in_dispencer = int(input())

while True:
    command = input()
    if command == 'Start':
        break
    people.append(command)

while True:
    command = input()
    if command == 'End':
        break
    if command.isnumeric() and len(people) > 0:
        liters_to_drink = int(command)
        person = people.popleft()
        if liters_to_drink <= liters_in_dispencer:
            liters_in_dispencer -= liters_to_drink
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
    elif command.startswith('refill '):
        liters_to_add = int(command.split()[-1])
        liters_in_dispencer += liters_to_add

print(f'{liters_in_dispencer} liters left')
