from collections import defaultdict

stock = defaultdict(int)

while True:
    tokens = input()
    if tokens == 'statistics':
        break
    k, v = tokens.split(':')[0], int(tokens.split(':')[1])
    stock[k] += v

print('Products in stock:')
for product in stock:
    print(f'- {product}: {stock[product]}')
print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')
