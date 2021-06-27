from collections import deque


def math_operations(*args, **kwargs):
    results = {
        'a': kwargs['a'],
        's': kwargs['s'],
        'd': kwargs['d'],
        'm': kwargs['m'],
    }

    numbers = deque(args)
    index = 0

    while numbers:
        num = numbers.popleft()

        if index == 0:
            results['a'] += num

        elif index == 1:
            results['s'] -= num

        elif index == 2:
            try:
                results['d'] /= num
            except ZeroDivisionError:
                index += 1
                if index > 3:
                    index = 0
                continue

        elif index == 3:
            results['m'] *= num

        index += 1
        if index > 3:
            index = 0

    return results


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))