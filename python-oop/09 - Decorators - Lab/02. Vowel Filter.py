from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        VOWELS = 'aeiouy'
        rv = function(*args, **kwargs)

        return [x for x in rv if x.lower() in VOWELS]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
