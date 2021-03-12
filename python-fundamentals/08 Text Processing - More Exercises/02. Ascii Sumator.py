c1 = input()
c2 = input()
random_string = input()
start = min(ord(c1), ord(c2))+1
end = max(ord(c1), ord(c2))
char_range = range(start, end)

total = 0

for char in random_string:
    if ord(char) in char_range:
        total += ord(char)

print(total)
