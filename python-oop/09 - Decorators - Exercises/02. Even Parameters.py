from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args):
        if not all(isinstance(a, int) and a % 2 == 0 for a in args):
            return f'Please use only even numbers!'

        rv = func(*args)

        return rv

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
