from collections import defaultdict

d = defaultdict(int)
tokens = input().split()
for e in tokens:
    d[e.lower()] += 1

odds = [e for e in d if d[e] % 2 != 0]
print(' '.join(odds))
