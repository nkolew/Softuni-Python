def compare_strings(data: list) -> tuple:
    s1 = data[0]
    s2 = data[1]
    if len(s1) == min(len(s1), len(s2)):
        return s1, s2
    return s2, s1


def multiply_char(strings: tuple) -> int:
    s, l = strings
    total = 0
    for i in range(len(l)):
        if i < len(s):
            total += ord(s[i])*ord(l[i])
        else:
            total += ord(l[i])
    return total


data = input().split()

print(multiply_char(compare_strings(data)))
