def repeat_by_len(l: list):
    result = ''
    for i in l:
        result += i * len(i)
    return result


strings = input().split()

print(repeat_by_len(strings))
