budget = float(input())
price_per_1kg_flour = float(input())

price_per_1pk_eggs = 0.75 * price_per_1kg_flour
price_per_1l_milk = 1.25 * price_per_1kg_flour

easter_bread_price = price_per_1kg_flour + \
    price_per_1pk_eggs + 0.250 * price_per_1l_milk

easter_breads_count = 0
colored_eggs = 0

while budget > 0:
    if easter_bread_price > budget:
        break
    budget -= easter_bread_price
    easter_breads_count += 1
    colored_eggs += 3
    if easter_breads_count % 3 == 0:
        colored_eggs -= (easter_breads_count - 2)

print(f'You made {easter_breads_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
