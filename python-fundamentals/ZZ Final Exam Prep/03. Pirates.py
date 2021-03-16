from collections import defaultdict


towns = defaultdict(dict)

while True:
    data = input()
    if data == 'Sail':
        break
    town, population, gold = data.split('||')
    if town not in towns:
        towns[town] = defaultdict(int)
    towns[town]['population'] += int(population)
    towns[town]['gold'] += int(gold)

while True:
    data = input()
    if data == 'End':
        break
    command, *tokens = data.split('=>')
    if command == 'Plunder':
        if len(towns) == 0:
            print('Ahoy, Captain! All targets have been plundered and destroyed!')
        town, people, gold = tokens
        towns[town]['population'] -= int(people)
        towns[town]['gold'] -= int(gold)
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if towns[town]['population'] == 0 or towns[town]['gold'] == 0:
            towns.pop(town)
            print(f'{town} has been wiped off the map!')
    if command == 'Prosper':
        town, gold = tokens
        if int(gold) < 0:
            print('Gold added cannot be a negative number!')
            continue
        towns[town]['gold'] += int(gold)
        print(
            f'{gold} gold added to the city treasury. {town} now has {towns[town]["gold"]} gold.')

print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')
for town_name, town_stats in sorted(towns.items(), key=lambda x : (-x[1]['gold'], x)):
    print(
        f'{town_name} -> Population: {town_stats["population"]} citizens, Gold: {town_stats["gold"]} kg')
