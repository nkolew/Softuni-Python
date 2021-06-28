GROW = 1
SHRINK = -1


def print_rhombus(n: int):

    def print_line(i, trend: int):

        if i == 0:
            return

        line: str = ' ' * (n-i) + '* ' * i
        print(line.rstrip())

        if i == n:
            trend = SHRINK

        print_line(i+trend, trend)

    print_line(1, GROW)


print_rhombus(int(input()))
