def create_numbers_dict():
    numbers_dict = {}

    while True:
        key = input()
        if key == 'Search':
            break

        value = input()
        if value == 'Search':
            break

        try:
            numbers_dict[key] = int(value)
        except ValueError:
            print("The variable number must be an integer")

    return numbers_dict


def search_number(numbers_dict: dict):
    message = []

    while True:
        key = input()
        if key == 'Remove':
            break

        try:
            message.append(str(numbers_dict[key]))
        except KeyError:
            message.append("Number does not exist in dictionary")

    return '\n'.join(message)


def remove_number(numbers_dict: dict):

    while True:
        key = input()
        if key == 'End':
            break

        try:
            numbers_dict.pop(key)
        except KeyError:
            print("Number does not exist in dictionary")

    return numbers_dict


numbers_dict = create_numbers_dict()

print(search_number(numbers_dict))

print(remove_number(numbers_dict))
