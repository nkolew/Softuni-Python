coffees_count = 0
command = input()

while not command == 'END':
    if command.lower() in ['coding', 'cat', 'dog', 'movie']:
        if command == command.lower():
            coffees_count += 1
        elif command == command.upper():
            coffees_count += 2
    command = input()

if coffees_count > 5:
    print('You need extra sleep')
else:
    print(coffees_count)
