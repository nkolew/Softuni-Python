def best_list_pureness(nums, k):
    from collections import deque

    def get_pureness(nums):
        return sum((i*n for i, n in enumerate(nums)))

    best_rotation = 0
    best_pureness = get_pureness(nums)
    nums = deque(nums)
    k = min(len(nums), k)

    for rotation in range(k+1):
        current_pureness = get_pureness(nums)

        if best_pureness < current_pureness:
            best_rotation = rotation
            best_pureness = current_pureness

        nums.rotate(1)

    return f'Best pureness {best_pureness} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
