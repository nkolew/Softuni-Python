def format_center(l):
    result = ()

    if sum([abs(l[0]), abs(l[1])]) <= sum([abs(l[2]), abs(l[3])]):
        return f'({int(l[0])}, {int(l[1])})({int(l[2])}, {int(l[3])})'

    return f'({int(l[2])}, {int(l[3])})({int(l[0])}, {int(l[1])})'


def calc_line_len(l):
    a = sum([abs(l[0]), abs(l[2])])
    b = sum([abs(l[1]), abs(l[3])])

    return (a**2 + b**2)**0.5


def comp_line_len(l1, l2, l1_len, l2_len):
    if l1_len >= l2_len:
        return l1

    return l2


l1 = [float(input()) for _ in range(4)]
l2 = [float(input()) for _ in range(4)]

l1_len = calc_line_len(l1)
l2_len = calc_line_len(l2)

longer_line = comp_line_len(l1, l2, l1_len, l2_len)

print(format_center(longer_line))
