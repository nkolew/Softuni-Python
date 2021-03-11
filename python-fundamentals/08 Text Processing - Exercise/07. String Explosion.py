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


# data = input()

# power = 0
# i = 0
# while i < len(data):
#     if data[i] == '>':
#         power += int(data[i+1])
#     else:
#         if power > 0:
#             data = data[:i] + data[i+1:]
#             power -= 1
#             i -= 1
#     i += 1

# print(data)