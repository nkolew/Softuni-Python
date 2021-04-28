from collections import deque

people = deque()

while True:
    command = input()
    if command == 'Paid':
        while len(people) > 0:
            print(people.popleft())
    elif command == 'End':
        break
    else:
        people.append(command)

print(f'{len(people)} people remaining.')
