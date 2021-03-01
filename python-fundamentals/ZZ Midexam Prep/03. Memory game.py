elements = input().split()
turns_count = 0
has_lost = True
while True:
    tokens = input()
    if tokens == 'end':
        break
    turns_count += 1
    i1, i2 = tokens.split()
    if not (
            i1 != i2 and
            0 <= int(i1) < len(elements) and
            0 <= int(i2) < len(elements)):
        half = len(elements)//2
        el = '-'+str(turns_count)+'a'
        elements.insert(half, el)
        elements.insert(half, el)
        print(f'Invalid input! Adding additional elements to the board')
    else:
        if elements[int(i1)] == elements[int(i2)]:
            e = elements[int(i1)]
            print(f'Congrats! You have found matching elements - {e}!')
            elements.pop(max([int(i1), int(i2)]))
            elements.pop(min([int(i1), int(i2)]))
            if len(elements) == 0:
                has_lost = False
                break
        else:
            print(f'Try again!')

if has_lost:
    print('Sorry you lose :(')
    print(' '.join(elements))
else:
    print(f'You have won in {turns_count} turns!')
