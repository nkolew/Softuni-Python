from typing import List, Set


def get_unique_items_from_input(n: int) -> Set[str]:
    return {input() for _ in range(n)}


def get_junct_of_two_sets(s1: Set[str], s2: Set[str]) -> Set[str]:
    return s1 & s2


def fmt_output(items: List[str]) -> str:
    nl = '\n'
    return nl.join(items)


def main() -> None:
    n, m = [int(x) for x in input().split()]
    s1 = get_unique_items_from_input(n)
    s2 = get_unique_items_from_input(m)
    s_junct = get_junct_of_two_sets(s1, s2)
    print(fmt_output(list(s_junct)))


main()
