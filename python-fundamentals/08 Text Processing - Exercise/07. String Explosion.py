data = input().split('>')
strength = 0
result = []
for word in data:
    if word[0].isdigit():
        strength += int(word[0])
        if strength > len(word):
            strength -= len(word)
            word = '>'
        else:
            word = '>'+word[strength::]
            strength = 0
    result.append(word)
print(''.join(result))
