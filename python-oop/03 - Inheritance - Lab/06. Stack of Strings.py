from typing import List


class Stack(list):
    def __init__(self) -> None:
        super().__init__()
        self.data: List[str] = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self) -> str:
        return f'[{", ".join(reversed(self.data))}]'

