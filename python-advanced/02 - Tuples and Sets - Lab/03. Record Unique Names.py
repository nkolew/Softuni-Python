def get_n_items(n: int) -> list:
    return [input() for _ in range(n)]


def get_unique_items(items: list) -> set:
    return set(items)


def fmt_output(items: set) -> str:
    nl = '\n'
    return nl.join([i for i in items])


def main() -> None:
    n = int(input())
    names = get_n_items(n)
    unique_names = get_unique_items(names)
    print(fmt_output(unique_names))


main()
