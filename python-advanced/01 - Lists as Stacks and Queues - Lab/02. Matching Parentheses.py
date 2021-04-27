s = input()

stack = []

for c in s:
    if c == '(':
        stack.append('')

    for i in range(len(stack)):
        stack[i] += c

    if c == ')':
        print(stack.pop())
