s = input()
result = ''
for i in range(len(s)):
    if (i+1 == len(s)) or (s[i] != s[i+1]):
        result += s[i]
print(result)
