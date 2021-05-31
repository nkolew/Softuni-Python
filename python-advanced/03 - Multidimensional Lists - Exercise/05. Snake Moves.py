from collections import deque

n, m = [int(x) for x in input().split()]
snake = deque(input())
arr = [['']*m for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            c = snake.popleft()
            arr[i][j] += c
            snake.append(c)
    else:
        for j in range(m-1, -1, -1):
            c = snake.popleft()
            arr[i][j] += c
            snake.append(c)

for row in arr:
    print(''.join(row))
