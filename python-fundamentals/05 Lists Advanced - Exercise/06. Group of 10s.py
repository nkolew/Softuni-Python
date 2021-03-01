def num_group_by_ten(l: list):
    groups = {}
    factor = 10

    while any(l):
        idx = 0
        while idx < len(l):
            if l[idx] is not None:
                if l[idx] <= factor:
                    if factor not in groups:
                        for empty in range(factor, 10, -10):
                            if empty not in groups:
                                groups[empty] = []
                        groups[factor] = []
                        groups[factor].append(l[idx])
                        l[idx] = None
                    else:
                        groups[factor].append(l[idx])
                        l[idx] = None
            idx += 1
        factor += 10
    return groups


numlist = list(map(int, input().split(', ')))

grouped_nums = num_group_by_ten(numlist)

for key in sorted(grouped_nums.keys()):
    print(f"Group of {key}'s: {grouped_nums[key]}")
