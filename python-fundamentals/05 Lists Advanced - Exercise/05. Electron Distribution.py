def dist_electrons(n: int):
    shell = [0]

    idx = 1
    while n > 0:

        vacancies = 2*idx**2

        if shell[idx-1] < vacancies:
            n -= 1
            shell[idx-1] += 1
        else:
            n -= 1
            shell.append(1)
            idx += 1

    return shell


electrons = int(input())

print(dist_electrons(electrons))
