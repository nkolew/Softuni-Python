children_count = 0
adults_count = 0
toy_price = 5
sweather_price = 15

command = input()
while command != 'Christmas':
    age = int(command)
    if age <= 16:
        children_count += 1
    else:
        adults_count += 1
    command = input()

print(f'Number of adults: {adults_count}')
print(f'Number of kids: {children_count}')
print(f'Money for toys: {children_count * toy_price}')
print(f'Money for sweaters: {adults_count * sweather_price}')
