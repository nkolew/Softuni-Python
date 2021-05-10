data = input()

stack = []
balanced = True

for c in data:
    if c in ['{', '(', '[']:
        stack.append(c)

    elif c in ['}', ')', ']']:
        if stack:
            c_prev = stack[-1]
            if ord(c) - ord(c_prev) in [1, 2]:
                stack.pop()
        else:
            balanced = False
            break

if not stack and balanced:
    print('YES')
else:
    print('NO')
