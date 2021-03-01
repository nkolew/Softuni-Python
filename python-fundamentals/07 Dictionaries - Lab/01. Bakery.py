tokens = input().split(' ')
bakery = {tokens[i]: int(tokens[i+1]) for i in range(0, len(tokens), 2)}
print(bakery)

# for i in range(0, len(tokens), 2):
#     bakery[tokens[i]] = int(tokens[i+1])
