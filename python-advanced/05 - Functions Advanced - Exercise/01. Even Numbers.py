def is_even(x):
    return x % 2 == 0


nums = [int(x) for x in input().split()]
print(list(filter(is_even, nums)))
