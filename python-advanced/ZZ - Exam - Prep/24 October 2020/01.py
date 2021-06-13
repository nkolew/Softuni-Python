from collections import deque

jobs = deque(int(x) for x in input().split(', '))
index = int(input())

threshold = jobs[index]
clock_cycles = 0

i = 0
end = len(jobs)
while True:
    if i == end:
        break

    job = jobs.popleft()
    if job <= threshold:
        clock_cycles += job
    i += 1

print(clock_cycles)
