def odd_and_even_sum(num):
    odd_list = []
    even_list = []

    for d in str(num):
        odd_list = [int(d) for d in str(num) if int(d) % 2 != 0]
        even_list = [int(d) for d in str(num) if int(d) % 2 == 0]

    return f'Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}'


number = int(input())

print(odd_and_even_sum(number))
