products = {}

while True:
    tokens = input()
    if tokens == 'buy':
        break
    name, price, quantity = tokens.split(' ')
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = {'price': price, 'quantity': quantity}
    else:
        products[name]['quantity'] += quantity
        if products[name]['price'] != price:
            products[name]['price'] = price

for product, data in products.items():
    total = data['price']*data['quantity']
    print(f'{product} -> {total:.2f}')
