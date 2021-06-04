items = input().split(', ')

d = {e: len(e) for e in items}

print(', '.join(f'{k} -> {v}' for k, v in {e: len(e) for e in items}.items()))
