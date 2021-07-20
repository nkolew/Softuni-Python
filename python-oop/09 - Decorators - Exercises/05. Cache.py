from functools import wraps


def cache(func):

    @wraps(func)
    def wrapper(n):

        rv = func(n)

        if n not in wrapper.log:
            wrapper.log[n] = rv

        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(44)
print(fibonacci.log)
