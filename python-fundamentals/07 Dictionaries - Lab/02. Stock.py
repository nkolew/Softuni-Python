from collections import defaultdict

tokens = input().split(' ')
stock = defaultdict(int)

for i in range(0, len(tokens), 2):
    stock[tokens[i]] += int(tokens[i+1])

products_needed = input().split(' ')

for product in products_needed:
    if product not in stock.keys():
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {stock[product]} of {product} left")
