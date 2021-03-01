population = list(map(int, input().split(',')))
min_wealth = int(input())
extra_money = True

while True:
    poor = 0
    wealthiest = 0
    poor_people = False
    if max(population) < min_wealth:
        extra_money = False
        break
    if min(population) >= min_wealth:
        break
    for index_poor, poor_person in enumerate(population):
        if poor_person < min_wealth:
            poor_people = True
            poor = index_poor

            for index_wealthy, wealthy_person in enumerate(population):
                if wealthy_person == max(population):
                    wealthiest = index_wealthy
            if population[wealthiest] == min_wealth:
                extra_money = False
                break
            population[poor] += 1
            population[wealthiest] -= 1

    if not extra_money:
        break
    if not poor_people:
        break

if poor_people:
    print('No equal distribution possible')
else:
    print(population)
