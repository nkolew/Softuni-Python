def str_repeat(s, r):
    result = ''

    for _ in range(r):
        result += s

    return result


string = input()
repeat = int(input())

print(str_repeat(string, repeat))
