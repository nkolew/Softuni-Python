from collections import defaultdict
from typing import DefaultDict, List


def get_occurences(nums: List[float]) -> dict:
    occurences: DefaultDict = defaultdict(int)
    for num in nums:
        occurences[num] += 1
    return occurences


def fmt_occurences(ocurrences: dict) -> str:
    result = []
    nl = '\n'
    for num, count in ocurrences.items():
        result.append(f'{num} - {count} times')
    return nl.join(result)


def main() -> None:
    numbers = list(map(float, input().split()))
    occurences = get_occurences(numbers)
    print(fmt_occurences(occurences))


main()
