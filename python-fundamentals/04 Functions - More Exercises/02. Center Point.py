def center_point(x1, y1, x2, y2):
    result = ()

    if sum([abs(x1), abs(y1)]) <= sum([abs(x2), abs(y2)]):
        return ((int(x1), int(y1)))

    return ((int(x2), int(y2)))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(center_point(x1, y1, x2, y2))
