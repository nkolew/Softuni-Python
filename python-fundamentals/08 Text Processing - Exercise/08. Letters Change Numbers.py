letter_map = {chr(97+i): i+1 for i in range(26)}
data = input().split()

result = 0
for word in data:
    let1 = word[0]
    let2 = word[-1]
    num = int(word[1:-1])
    if let1.isupper():
        num /= letter_map[let1.lower()]
    else:
        num *= letter_map[let1]
    if let2.isupper():
        num -= letter_map[let2.lower()]
    else:
        num += letter_map[let2]
    result += num

print(f'{result:.2f}')
