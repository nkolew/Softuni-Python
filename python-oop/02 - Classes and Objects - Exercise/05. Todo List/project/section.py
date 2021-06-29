from typing import List
from task import Task


class Section:
    tasks: List[Task] = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_task(self, new_task: Task) -> str:
        if new_task in Section.tasks:
            return f'Task is already in the section {self.name}'

        Section.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str) -> str:
        for task in Section.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self) -> str:
        cleared_tasks = 0
        i = 0
        end = len(Section.tasks)
        while i < end:
            task = Section.tasks[i]
            if task.completed:
                Section.tasks.pop(i)
                cleared_tasks += 1
            i += 1
        return f'Cleared {cleared_tasks} tasks.'

    def view_section(self) -> str:
        message = []
        nl = '\n'
        message.append(f'Section {self.name}:')
        for task in Section.tasks:
            message.append(task.details())
        return nl.join(message)
