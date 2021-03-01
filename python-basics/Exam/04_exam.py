cats_count = int(input())

food_price_per_kg = 12.45
small_cats = 0
big_cats = 0
large_cats = 0
total_food = 0

for cat in range(cats_count):
    food = float(input())
    if 100 <= food < 200:
        small_cats += 1
        total_food += food
    elif 200 <= food < 300:
        big_cats += 1
        total_food += food
    elif 300 <= food < 400:
        large_cats += 1
        total_food += food

total_food_in_kg = total_food / 1000
food_price = total_food_in_kg * food_price_per_kg

print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {large_cats} cats.')
print(f'Price for food per day: {food_price:.2f} lv.')
