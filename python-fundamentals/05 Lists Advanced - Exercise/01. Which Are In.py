def which_are_in(subs: list, string: str):

    return [sub for sub in subs if sub in string]


subs = input().split(', ')
string = input()

print(which_are_in(subs, string))
