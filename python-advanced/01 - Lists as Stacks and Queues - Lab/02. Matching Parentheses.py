from collections import deque


brackets = deque()
expr = input()

for i, c in enumerate(expr):
    if c == '(':
        brackets.append(i)
    elif c == ')':
        start = brackets.pop()
        print(expr[start:i+1])


# s = input()

# stack = []

# for c in s:
#     if c == '(':
#         stack.append('')

#     for i in range(len(stack)):
#         stack[i] += c

#     if c == ')':
#         print(stack.pop())
