def item_exists(l: list, s: str):
    if l.count(s):
        return True
    return False


def collect(l: list, s: str):
    if item_exists(l, s):
        return l
    l.append(s)
    return l


def drop(l: list, s: str):
    if item_exists(l, s):
        l.remove(s)
    return l


def combine(l: list, old: str, new: str):
    if item_exists(l, old):
        l.insert((l.index(old)+1), new)
    return l


def renew(l: list, s: str):
    if item_exists(l, s):
        l.remove(s)
        l.append(s)
    return l


journal = input().split(', ')
command_data = input()

while command_data != 'Craft!':
    command, item = command_data.split(' - ')
    if command == 'Collect':
        journal = collect(journal, item)
    elif command == 'Drop':
        journal = drop(journal, item)
    elif command == 'Combine Items':
        old, new = item.split(':')
        journal = combine(journal, old, new)
    elif command == 'Renew':
        journal = renew(journal, item)

    command_data = input()

print(', '.join(journal))
