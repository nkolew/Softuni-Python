number = int(input())
for top_row in range(1, number+1):
    print('*'*top_row)
for bottom_row in range(number-1, 0, -1):
    print('*'*bottom_row)