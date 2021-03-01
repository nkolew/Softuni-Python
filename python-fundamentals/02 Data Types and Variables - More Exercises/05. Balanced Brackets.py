lines_count = int(input())

brackets_list = [0]

balanced = True

for line in range(lines_count):

    string = input()

    if string not in ['(', ')']:
        continue

    elif string == '(':
        if brackets_list[-1] == '(':
            balanced = False
            break

        brackets_list.append(string)

    elif string == ')':
        if brackets_list[-1] == ')':
            balanced = False
            break

        brackets_list.append(string)

if not brackets_list.count('(') == brackets_list.count(')'):
    balanced = False

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
