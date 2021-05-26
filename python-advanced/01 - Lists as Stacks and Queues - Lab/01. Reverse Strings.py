from collections import deque


s = deque(input())

while s:
    print(s.pop(), end='')
