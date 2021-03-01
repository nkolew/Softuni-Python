parking = {}

n = int(input())

for _ in range(n):
    tokens = input()
    command, username = tokens.split()[0], tokens.split()[1]
    if command == 'register':
        license_plate = tokens.split()[2]
        if username not in parking:
            parking[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
        else:
            print(
                f'ERROR: already registered with plate number {parking[username]}')
    elif command == 'unregister':
        if username not in parking:
            print(f'ERROR: user {username} not found')
        else:
            parking.pop(username)
            print(f'{username} unregistered successfully')


print('\n'.join([f'{username} => {license_plate}'for username,
                 license_plate in parking.items()]))
