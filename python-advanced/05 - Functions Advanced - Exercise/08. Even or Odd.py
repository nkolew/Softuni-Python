def even_odd(*args):
    ops = {
        'even': lambda x: x % 2 == 0,
        'odd': lambda x: x % 2 == 1,
    }
    op = args[-1]
    nums = args[0:-1]

    return list(filter(ops[op], nums))
