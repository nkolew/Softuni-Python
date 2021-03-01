CLOTHES_MAX_PRICE = 50.0
SHOES_MAX_PRICE = 35.0
ACCESSORIES_MAX_PRICE = 20.50
TARGET_MONEY = 150.0

items = input().split('|')
budget = float(input())


items_bought = []
profit = 0

for item in items:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    if item_type == 'Clothes' and item_price > CLOTHES_MAX_PRICE:
        continue

    elif item_type == 'Shoes' and item_price > SHOES_MAX_PRICE:
        continue

    elif item_type == 'Accessories' and item_price > ACCESSORIES_MAX_PRICE:
        continue

    if budget < item_price:
        continue

    budget -= item_price
    current_profit = item_price * 0.4
    profit += current_profit
    items_bought.append(item_price+current_profit)


print(' '.join([format(price, '.2f') for price in items_bought]))

print(f'Profit: {profit:.2f}')

if budget + sum(items_bought) >= TARGET_MONEY:
    print('Hello, France!')
else:
    print('Time to go.')
