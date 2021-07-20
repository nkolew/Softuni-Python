from functools import wraps


def multiply(times):

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            rv = function(*args, **kwargs)
            return times * rv

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
