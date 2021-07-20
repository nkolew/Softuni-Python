from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        rv = func(*args, **kwargs)
        args_str = ', '.join([str(x) for x in args])
        return f'you called {func.__name__}({args_str})\nit returned {rv}'
    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
