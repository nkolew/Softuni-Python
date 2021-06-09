from itertools import combinations

names = input().split(', ')
n = int(input())

for combo in combinations(names, n):
    print(', '.join(combo))