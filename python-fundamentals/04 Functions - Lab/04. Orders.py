COFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00


def order_price(type, quantity):
    price = None

    if type == 'coffee':
        price = COFEE_PRICE * quantity

    if type == 'water':
        price = WATER_PRICE * quantity

    if type == 'coke':
        price = COKE_PRICE * quantity

    if type == 'snacks':
        price = SNACKS_PRICE * quantity
 
    return f'{price:.2f}'


what = input()
how_many = float(input())

print(order_price(what,how_many))
