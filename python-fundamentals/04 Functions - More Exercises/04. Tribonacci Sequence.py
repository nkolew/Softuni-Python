def find_tribonacci(number):
    t_nums = [1]

    num = 1
    while len(t_nums) < number:

        if len(t_nums) < 3:

            if len(t_nums) == 1:
                if num == t_nums[-1] + 0 + 0:
                    t_nums.append(num)
            elif len(t_nums) == 2:
                if num == t_nums[-1] + t_nums[-2] + 0:
                    t_nums.append(num)
        else:
            if num == t_nums[-1] + t_nums[-2] + t_nums[-3]:
                t_nums.append(num)

        num += 1

    return t_nums


def print_tribonacci(l):
    print(' '.join(map(str, l)))


num = int(input())

numlist = find_tribonacci(num)
print_tribonacci(numlist)
