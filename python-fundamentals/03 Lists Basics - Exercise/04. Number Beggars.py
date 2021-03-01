numbers_list = [int(num) for num in input().split(', ')]
beggars_count = int(input())

beggars_list = []

start_index = 0

for beggar in range(beggars_count):

    beggar_sum = 0

    for index in range(start_index, len(numbers_list), beggars_count):

        beggar_sum += numbers_list[index]

    beggars_list.append(beggar_sum)

    start_index += 1


print(beggars_list)

# beggars_list = [0 for beggar in range(beggars_count)]

# count = 0

# for number in numbers_list:

#     beggars_list[count] += number

#     count += 1

#     if count >= beggars_count:
#         count = 0

# print(beggars_list)
