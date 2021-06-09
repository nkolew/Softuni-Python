from functools import reduce


def multiply(*args):
    return reduce(lambda a, b: a*b, args)
