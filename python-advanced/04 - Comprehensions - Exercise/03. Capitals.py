countries = input().split(', ')
capitals = input().split(', ')

d = {i: j for i, j in zip(countries, capitals)}

print('\n'.join(f'{i} -> {j}' for i, j in d.items()))
