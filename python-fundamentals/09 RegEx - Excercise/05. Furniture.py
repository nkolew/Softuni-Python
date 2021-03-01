import re

bought_furniture = []
total_price = 0

pattern = r'(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!((?P<quantity>\d+)$)'

while True:
    line = input()
    if line == 'Purchase':
        break
    match = re.match(pattern, line)
    if match:
        bought_furniture.append(match.groupdict()['name'])
        total_price += float(match.groupdict()['price']) * int(match.groupdict()['quantity'])

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_price:.2f}')