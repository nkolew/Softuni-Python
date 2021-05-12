from collections import defaultdict
from typing import DefaultDict, Dict, List


def get_n_items(n: int) -> list:
    return [input() for _ in range(n)]


def parse_items_to_dict(items: List[str]) -> Dict[str, List[float]]:
    grades: DefaultDict = defaultdict(list)
    for item in items:
        name, grade = item.split()
        grades[name].append(float(grade))
    return grades


def get_avg_grade(grade_list: List[float]) -> float:
    return sum(grade_list) / len(grade_list)


def fmt_output(grades: dict) -> str:
    result = []
    nl = '\n'
    for name, grade_list in grades.items():
        grades_str = ' '.join(map(lambda x: format(x, '.2f'), grade_list))
        avg_grade = get_avg_grade(grade_list)
        result.append(f'{name} -> {grades_str} (avg: {avg_grade:.2f})')
    return nl.join(result)


def main() -> None:
    n = int(input())
    data = get_n_items(n)
    grades = parse_items_to_dict(data)
    print(fmt_output(grades))


main()
