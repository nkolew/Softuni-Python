from typing import List, Set


def get_n_items(n: int) -> List[str]:
    return [input() for _ in range(n)]


def get_unique_elements(items: List[str]) -> Set[str]:
    return {el for item in items for el in item.split()}


def fmt_output(items: List[str]) -> str:
    nl = '\n'
    return nl.join(items)


def main() -> None:
    n = int(input())
    compound_list = get_n_items(n)
    elements = get_unique_elements(compound_list)
    print(fmt_output(list(elements)))


main()
