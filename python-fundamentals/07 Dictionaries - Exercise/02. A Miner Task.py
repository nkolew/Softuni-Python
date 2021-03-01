from collections import defaultdict


resources = defaultdict(int)

while True:
    token = input()
    if token == 'stop':
        break
    resource = token
    quantity = int(input())
    resources[resource] += quantity

for r, v in resources.items():
    print(f'{r} -> {v}')
