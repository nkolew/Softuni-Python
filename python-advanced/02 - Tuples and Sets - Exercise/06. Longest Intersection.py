from typing import List, Set


def get_n_items(n: int) -> List[str]:
    return [input() for _ in range(n)]


def parse_junctions_data(l: List[str]) -> List[Set]:
    junctions: List[Set[int]] = []
    for item in l:
        r1, r2 = item.split('-')
        r1_s, r1_e = r1.split(',')
        r2_s, r2_e = r2.split(',')
        range1 = {x for x in range(int(r1_s), int(r1_e)+1)}
        range2 = {x for x in range(int(r2_s), int(r2_e)+1)}
        junctions.append(range1 & range2)
    return junctions


def get_max_junction(l: List[Set]) -> Set[int]:
    max_len = max([len(x) for x in l])
    for s in l:
        if len(s) == max_len:
            return s
    return set()


def fmt_output(s: Set[int]) -> str:
    return f'Longest intersection is {list(s)} with length {len(s)}'


def main() -> None:
    n = int(input())
    data = get_n_items(n)
    junctions = parse_junctions_data(data)
    max_junct = get_max_junction(junctions)
    print(fmt_output(max_junct))


main()
