def flatten(s):
    return ' '.join((j for i in reversed(s.split('|')) for j in i.split()))


s = input()
print(flatten(s))
