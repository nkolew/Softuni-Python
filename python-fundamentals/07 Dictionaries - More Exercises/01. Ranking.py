from collections import defaultdict


auth = {}
contests = defaultdict(list)

while True:
    data = input()
    if data == 'end of contests':
        break
    contest, password = data.split(':')
    auth[contest] = password

while True:
    data = input()
    if data == 'end of submissions':
        break
    contest, password, username, points = data.split('=>')
    points = int(points)
    if contest in auth:
        if auth[contest] == password:
            if username not in contests:
                contests[username].append(
                    {'contest': contest, 'points': points})
            else:
                new_contest = True
                for i in range(len(contests[username])):
                    c = contests[username][i]['contest']
                    p = contests[username][i]['points']
                    if c == contest:
                        new_contest = False
                        if p < points:
                            contests[username][i]['points'] = points
                        break
                if new_contest:
                    contests[username].append(
                        {'contest': contest, 'points': points})

users_total_points = defaultdict(int)

for username, data in contests.items():
    for i in range(len(data)):
        users_total_points[username] += contests[username][i]['points']

for username, points in users_total_points.items():
    if points == max(users_total_points.values()):
        print(f'Best candidate is {username} with total {points} points.')

print('Ranking:')

for username, data in sorted(contests.items()):
    print(username)
    
    for tokens in sorted(data, key=lambda x: -x['points']):
        contest = tokens['contest']
        points = tokens['points']
        print(f'#  {contest} -> {points}')
