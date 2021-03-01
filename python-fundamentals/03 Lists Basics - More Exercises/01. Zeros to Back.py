num_list = [int(num) for num in input().split(', ')]

for idx in range(len(num_list)-1, -1, -1):
    if num_list[idx] == 0:
        zero = num_list.pop(idx)
        num_list.append(zero)

print(num_list)
