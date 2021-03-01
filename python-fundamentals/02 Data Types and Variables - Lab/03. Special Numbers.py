n = int(input())

for num in range(1, n+1):
    dig_list = [int(dig) for dig in str(num)]
    if sum(dig_list) in [5, 7, 11]:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
