n = int(input())
stack = []

for _ in range(n):
    command = input()
    if command.startswith('1 '):
        stack.append(int(command.split()[-1]))
    elif command == '2' and stack:
        stack.pop()
    elif command.startswith('3') and stack:
        print(max(stack))
    elif command.startswith('4') and stack:
        print(min(stack))
result = []
while stack:
    result.append(stack.pop())

print(*result, sep=', ')
