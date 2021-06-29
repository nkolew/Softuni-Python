class Task:
    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)

    def change_name(self, new_name: str):
        if self.name == new_name:
            return 'Name cannot be the same.'
        self.name = new_name
        return f'{new_name}'

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return 'Date cannot be the same.'
        self.due_date = new_date
        return f'{new_date}'

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number >= len(self.comments):
            return 'Cannot find comment.'

        self.comments.pop(comment_number)
        self.comments.insert(comment_number, new_comment)

        return ', '.join(self.comments)

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'
