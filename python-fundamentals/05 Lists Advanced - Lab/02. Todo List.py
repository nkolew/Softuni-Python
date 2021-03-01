todo_list = {}

command_data = input()
while command_data != 'End':
    priority, errand, = command_data.split('-')
    priority = int(priority)

    todo_list[priority] = errand

    command_data = input()

todo_list_sorted = [todo_list[k] for k in sorted(todo_list)]
print(todo_list_sorted)
