from typing import List, Set, Tuple


def get_n_items(n: int) -> List[str]:
    return [input() for _ in range(n)]


def parse_names(l: List) -> Tuple[Set[int], Set[int]]:
    odds = set()
    evens = set()
    for i, name in enumerate(l):
        name_num = 0
        for c in name:
            name_num += ord(c)
        name_num //= (i+1)
        if name_num % 2 == 0:
            evens.add(name_num)
        else:
            odds.add(name_num)
    return (odds, evens)


def get_name_nums(odds: Set[int], evens: Set[int]) -> List[int]:
    odd_sum = sum(x for x in odds)
    even_sum = sum(x for x in evens)
    if odd_sum < even_sum:
        return list(odds ^ evens)
    elif odd_sum > even_sum:
        return list(odds - evens)
    return list(odds | evens)


def fmt_output(l: List[int]) -> str:
    return ', '.join(map(str, l))


def main() -> None:
    n = int(input())
    data = get_n_items(n)
    odds, evens = parse_names(data)
    name_nums = get_name_nums(odds, evens)
    print(fmt_output(name_nums))


main()
