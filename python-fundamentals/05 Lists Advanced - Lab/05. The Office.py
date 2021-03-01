def chk_happiness(l: list, f: int):

    l_f = list(map(lambda x: x*f, l))

    happy = list(filter(lambda x: x >= (sum(l_f)/len(l_f)), l_f))

    if len(happy) >= len(l)/2:

        return (f'{len(happy)}/{len(l)}', True)

    return (f'{len(happy)}/{len(l)}', False)


happiness_list = list(map(int, input().split()))
factor = int(input())

score, happy_office = chk_happiness(happiness_list, factor)

if happy_office:
    print(f'Score: {score}. Employees are happy!')

else:
    print(f'Score: {score}. Employees are not happy!')
