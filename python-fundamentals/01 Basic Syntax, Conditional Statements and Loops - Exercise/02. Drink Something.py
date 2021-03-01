age = int(input())
drink = ''

if age <= 14:
    drink = 'toddy'
elif age <= 18:
    drink = 'coke'
elif age < 22:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')
