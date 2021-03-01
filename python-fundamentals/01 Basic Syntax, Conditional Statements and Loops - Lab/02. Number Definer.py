num = float(input())

if num < - 1000000:
    print('large negative')
elif - 1000000 <= num <= -1:
    print('negative')
elif -1 < num < 0:
    print('small negative')
elif num == 0:
    print('zero')
elif 0 < num < 1:
    print('small positive')
elif 1 <= num <= 1000000:
    print('positive')
else:
    print('large positive')
