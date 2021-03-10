def validate(s: str):
    if not (3 <= len(s) <= 16):
        return False
    for c in s:
        if not (c.isalnum() or c in ['-', '_']):
            return False
    return True


data = input().split(', ')

for name in filter(validate, data):
    print(name)
