import re


RDI = 2000


food = []

pattern = r'(?P<sym>#|\|)(?P<food>[A-Za-z ]+)(?P=sym)(?P<exp>\d{2}/\d{2}/\d{2})(?P=sym)(?P<cal>\d{1,5})(?P=sym)'

data = input()

for m in re.finditer(pattern, data):
    name = m.group('food')
    exp_date = m.group('exp')
    calories = int(m.group('cal'))
    food.append({'name': name, 'exp_date': exp_date, 'calories': calories})

total_calories = sum(i['calories'] for i in food)
days = total_calories // RDI
print(f'You have food to last you for: {days} days!')
for food in food:
    print(
        f'Item: {food["name"]}, Best before: {food["exp_date"]}, Nutrition: {food["calories"]}')
