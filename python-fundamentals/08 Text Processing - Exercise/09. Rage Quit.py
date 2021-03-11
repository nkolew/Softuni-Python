data = input()

i = 0
rage = ''
result = ''
while i < len(data):
    if data[i].isdigit():
        num = data[i]
        if i+1 < len(data) and data[i+1].isdigit():
            num += data[i+1]
            i += 1
        cnt = int(num)
        current_rage = rage*cnt
        result += current_rage
        rage = ''
    else:
        rage += data[i].upper()
    i += 1

print(f'Unique symbols used: {len(set(result))}')
print(result)
