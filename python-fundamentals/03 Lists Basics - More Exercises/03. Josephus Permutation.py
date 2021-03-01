initial_sequence = input().split(' ')
k = int(input())

result_list = []
counter = 0

index = 0
while len(initial_sequence) > 0:
    counter += 1

    if counter % k == 0:
        result_list.append(initial_sequence.pop(index))
    else:
        index += 1

    if index >= len(initial_sequence):
        index = 0

print(str(result_list).replace(' ','').replace('\'',''))
