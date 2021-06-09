# from itertools import chain, combinations, permutations, product

# nums = input().split(', ')
# n = len(nums)

# for p in product('+-', repeat=n):
#     el = (''.join(x) for x in zip(p, nums))
#     expr = ''.join(el)
#     print(f'{expr}={eval(expr)}')


# perms = set(permutations(['+']*n+['-']*n, n))

# for perm in perms:
#     expr = ''.join(chain(*zip(perm, nums)))
#     res = eval(expr)
#     print(f'{expr}={res}')


def expr(numbers, cur_res=0, cur_exp=''):
    if not numbers:
        print(f'{cur_exp} = {cur_res}')
        return
    expr(numbers[1:], cur_res+numbers[0], f'{cur_exp}+{numbers[0]}')
    expr(numbers[1:], cur_res-numbers[0], f'{cur_exp}-{numbers[0]}')


numbers = [int(x) for x in input().split(', ')]
expr(numbers)