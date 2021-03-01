n = int(input())
word = input()

all_strings = []
matched_strings = []

for _ in range(n):
    
    string = input()

    all_strings.append(string)

    if word in string:
        matched_strings.append(string)

print(all_strings)
print(matched_strings)