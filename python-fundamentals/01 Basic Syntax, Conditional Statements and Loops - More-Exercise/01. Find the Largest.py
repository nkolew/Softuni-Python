num = input()

dig_list = [dig for dig in str(num) if dig.isnumeric()]
dig_list.sort(reverse=True)

print(''.join(dig_list))