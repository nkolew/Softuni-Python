targets = list(map(int, input().split()))

while True:
    token = input()
    if token == 'End':
        break
    idx = int(token)
    if 0 <= idx < len(targets):
        if targets[idx] == -1:
            continue
        threshold = targets[idx]
        targets[idx] = -1
        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            if targets[i] > threshold:
                targets[i] -= threshold
            else:
                targets[i] += threshold

print(f'Shot targets: {targets.count(-1)} -> {" ".join(map(str, targets))}')
