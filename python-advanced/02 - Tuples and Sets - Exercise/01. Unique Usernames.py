from typing import List


def get_n_items(n: int) -> List[str]:
    return [input() for _ in range(n)]


def fmt_output(users: List[str]) -> str:
    nl = '\n'
    return nl.join(users)


def main() -> None:
    n = int(input())
    users = get_n_items(n)
    unique_users = set(users)
    print(fmt_output(list(unique_users)))


main()
