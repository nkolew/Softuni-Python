def add(n1, n2):

    return n1 + n2


def subtract(res, n3):
    
    return res - n3


def add_and_subtract(n1, n2, n3):
    res = add(n1, n2)

    return subtract(res, n3)


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
