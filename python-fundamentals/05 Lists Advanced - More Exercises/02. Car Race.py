times_list = list(map(int, input().split()))
center = len(times_list) // 2
left_time = 0
right_time = 0
for left in times_list[:center]:
    if left == 0:
        left_time *= 0.8
    else:
        left_time += left
for right in reversed(times_list[center+1:]):
    if right == 0:
        right_time *= 0.8
    else:
        right_time += right
time = min([left_time, right_time])
if left_time == time:
    winner = 'left'
else:
    winner = 'right'
print(f'The winner is {winner} with total time: {time:.1f}')
