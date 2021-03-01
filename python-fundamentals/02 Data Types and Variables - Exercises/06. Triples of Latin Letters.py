chars_count = int(input())

for char_one in range(97,97 + chars_count):
    for char_two in range(97, 97 + chars_count):
        for char_three in range(97, 97 + chars_count):
            print(f'{chr(char_one)}{chr(char_two)}{chr(char_three)}')