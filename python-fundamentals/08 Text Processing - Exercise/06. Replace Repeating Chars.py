text = input()
i = 0
result = ''

for i in range(len(text)):
    if i + 1 == len(text) or text[i] != text[i+1]:
        result += text[i]


print(result)
