def get_matching_chars(s: str, condition_fn):
    result = ''
    for char in s:
        if condition_fn(char):
            result += char
    return result


def all_digits(s: str):
    return get_matching_chars(
        s,
        lambda c: c.isdigit()
    )


def all_letters(s: str):
    return get_matching_chars(
        s,
        lambda c: c.isalpha()
    )


def all_others(s: str):
    return get_matching_chars(
        s,
        lambda c: not c.isalnum()
    )


s = input()

print(all_digits(s))
print(all_letters(s))
print(all_others(s))
