chars_count = int(input())

chars_sum = 0

for i in range(0, chars_count):
    char = input()
    chars_sum += ord(char)

print(f'The sum equals: {chars_sum}')