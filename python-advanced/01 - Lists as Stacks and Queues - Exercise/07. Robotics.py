from collections import deque
from datetime import datetime, timedelta
from typing import Dict, List


robots_data: List[str] = input().split(';')
robots: List[Dict] = []

for i in range(len(robots_data)):
    robot_tokens = robots_data[i].split('-')
    robots.append({
        'name': robot_tokens[0],
        'proc_time': int(robot_tokens[1]),
        'avail_at': 0,
    })

start_time = datetime.strptime(input(), '%H:%M:%S')

items = deque()

while True:
    next_item = input()
    if next_item == 'End':
        break
    items.append(next_item)

current_time = 0

while items:
    current_time += 1
    next_item = items.popleft()

    for index, robot in enumerate(robots):
        if robot['avail_at'] <= current_time:
            robots[index]['avail_at'] = current_time + robot['proc_time']
            robot_name = robot['name']
            time_str = (start_time + timedelta(seconds=current_time)
                        ).strftime('%H:%M:%S')
            print(f'{robot_name} - {next_item} [{time_str}]')
            break
    else:
        items.append(next_item)
