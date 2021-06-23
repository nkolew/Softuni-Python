def numbers_searching(*args):

    nums_count = {num: 0 for num in args}

    for n in args:
        nums_count[n] += 1

    duplicates = [n for n, c in nums_count.items() if c > 1]
    missing = None

    min_val = min(args)
    max_val = max(args)

    for i in range(min_val, max_val+1):
        if i not in nums_count:
            missing = i

    return [missing, sorted(duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48,
      45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
