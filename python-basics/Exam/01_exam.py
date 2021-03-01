price_per_page = float(input())
price_per_cover = float(input())
printing_discount = int(input())
designer_fee = float(input())
crew_percentage = int(input())

money = price_per_page * 899 + price_per_cover * 2
money = money - printing_discount * money / 100
money += designer_fee
money = money - crew_percentage * money / 100

print(f"Avtonom should pay {money:.2f} BGN.")
