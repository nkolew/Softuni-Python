force = {}

while True:
    user_exists = False
    data = input()
    if data == 'Lumpawaroo':
        break
    if ' | ' in data:
        side, user = data.split(' | ')
        if side not in force:
            force[side] = []
            for side, users in force.items():
                for u in users:
                    if u == user:
                        user_exists = True
                        break
                if user_exists:
                    break
            if user_exists:
                continue
        if user not in force[side]:
            force[side].append(user)
    elif ' -> ' in data:
        user, side = data.split(' -> ')
        if side not in force:
            force[side] = []
        if user not in force[side]:
            force[side].append(user)
            for s, users in force.items():
                if s != side:
                    while user in users:
                        force[s].remove(user)

            print(f'{user} joins the {side} side!')


for side, users in sorted(force.items(), key=lambda x: (-len(x[1]), x[0])):
    if users:
        print(f'Side: {side}, Members: {len(users)}')
    for user in sorted(users):
        print(f'! {user}')
