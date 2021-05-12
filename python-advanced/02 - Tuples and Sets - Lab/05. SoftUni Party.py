def get_n_items(n: int) -> list:
    return [input() for _ in range(n)]


def get_items_until_stop(stop: str) -> list:
    items = []
    while True:
        item = input()
        if item == stop:
            return items
        items.append(item)


def get_guests_not_attd(resv, attd):
    return set(resv) ^ set(attd)


def fmt_guests(guests: set) -> str:
    nl = '\n'
    return f'{len(guests)}' + nl + f'{nl.join(sorted(guests))}'


def main():
    n = int(input())
    resv = get_n_items(n)
    attd = get_items_until_stop('END')
    notattd_guests = get_guests_not_attd(resv, attd)
    print(fmt_guests(notattd_guests))


main()
