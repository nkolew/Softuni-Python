from collections import defaultdict


players = defaultdict(dict)

while True:
    data = input()
    if data == 'Season end':
        break
    if ' -> ' in data:
        player, position, skill = data.split(' -> ')
        skill = int(skill)
        new = True
        for p in players:
            if p == player:
                for ps, sk in players[p].items():
                    if ps == position:
                        new = False
                        if sk < skill:
                            players[player][position] = skill
        if new:
            players[player][position] = skill
    elif ' vs ' in data:
        player1, player2 = data.split(' vs ')
        found = False
        if player1 in players and player2 in players:
            for ps1, sk1 in players[player1].items():
                for ps2, sk2 in players[player2].items():
                    if ps1 == ps2:
                        found = True
                        player1_total = sum(players[player1].values())
                        player2_total = sum(players[player2].values())
                        if player1_total > player2_total:
                            players.pop(player2)
                        elif player1_total < player2_total:
                            players.pop(player1)
                    if found:
                        break
                if found:
                    break

for player in sorted(players, key=lambda p: -sum(players[p].values())):
    total = sum(players[player].values())
    print(f'{player}: {total} skill')
    for position, skill in sorted(players[player].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {position} <::> {skill}')
