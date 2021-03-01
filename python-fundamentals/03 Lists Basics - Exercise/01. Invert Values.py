orig_list = input().split()

inverted_list = []

for num in orig_list:

    if int(num) > 0:
        inverted_list.append(int('-'+ num))

    elif int(num) < 0:
        inverted_list.append(abs(int(num)))
    
    else:
        inverted_list.append(int(num))

print(inverted_list)