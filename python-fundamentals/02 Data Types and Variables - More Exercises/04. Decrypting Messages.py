key = int(input())
lines_count = int(input())

chars_list = []

for line in range(lines_count):
    char = input()
    chars_list.append(chr(ord(char)+key))

message = ''.join(chars_list)
print(message)
