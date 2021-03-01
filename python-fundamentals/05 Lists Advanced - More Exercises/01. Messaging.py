nums_list = list(map(int, input().split()))
string = list(input())

idx = []
for num in nums_list:
    sum_of_digits = 0
    str_num = str(num)
    for d in str_num:
        sum_of_digits += int(d)
    idx.append(sum_of_digits)

message = []
for i in idx:
    if i > len(string):
        i -= len(string)
    message.append(string.pop(i))

print(f'{"".join(message)}')
