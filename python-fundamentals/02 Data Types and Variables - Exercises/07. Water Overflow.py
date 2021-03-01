CAPACITY = 255

fillups = int(input())

total_quantity = 0

for fillup in range(fillups):
    quantity = int(input())
    if total_quantity + quantity > CAPACITY:
        print('Insufficient capacity!')
    else:
        total_quantity += quantity

print(total_quantity)