def chars_in_range(c1, c2):
    if ord(c1) > ord(c2):
        c1, c2 = c2, c1

    return ' '.join([chr(num) for num in range(ord(c1)+1, ord(c2))])


char1 = input()
char2 = input()

print(chars_in_range(char1, char2))
