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


# from heapq import heappop

# tasks = [int(x) for x in input().split(', ')]
# index = int(input())

# searched_task = tasks[index]

# clock_cycles = 0
# while (task := heappop(tasks)) <= searched_task:
#     clock_cycles += task

# print(clock_cycles)
