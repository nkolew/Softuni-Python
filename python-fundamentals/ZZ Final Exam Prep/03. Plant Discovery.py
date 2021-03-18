plants = {}

n = int(input())
for _ in range(n):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    plants[plant] = {'rarity': rarity}

while True:
    data = input()
    if data == 'Exhibition':
        break
    command, tokens = data.split(': ')
    if command == 'Rate':
        try:
            plant, rating = tokens.split(' - ')
            rating = int(rating)
            if 'ratings' not in plants[plant]:
                plants[plant]['ratings'] = []
            plants[plant]['ratings'].append(rating)
        except:
            print('error')
    elif command == 'Update':
        try:
            plant, new_rarity = tokens.split(' - ')
            new_rarity = int(new_rarity)
            plants[plant]['rarity'] = new_rarity
        except:
            print('error')
    elif command == 'Reset':
        try:
            plant = tokens
            if 'ratings' in plants[plant]:
                plants[plant].pop('ratings')
            else:
                print('error')
                continue
        except:
            print('error')
    else:
        print('error')
        continue

for name, stats in plants.items():
    if 'ratings' not in stats:
        stats['av_rating'] = 0
    else:
        stats['av_rating'] = sum(
            stats['ratings'])/len(stats['ratings'])

print('Plants for the exhibition:')
for name, stats in sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['av_rating'])):
    print(
        f'- {name}; Rarity: {stats["rarity"]}; Rating: {stats["av_rating"]:.2f}')
