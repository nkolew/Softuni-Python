def chr_multiplier(s1: str, s2: str):
    result = 0

    long = max((len(s1), len(s2)))

    for i in range(long):
        if i >= len(s1):
            result += ord(s2[i])
        elif i >= len(s2):
            result += ord(s1[i])
        else:
            result += ord(s1[i])*ord(s2[i])
    return result


strings = input().split()
s1 = strings[0]
s2 = strings[1]

print(chr_multiplier(s1, s2))
