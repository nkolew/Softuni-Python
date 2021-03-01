def filter_usernames(l: list):
    filtered = []
    for username in l:
        valid_name = True
        if not (3 <= len(username) <= 16):
            valid_name = False
            continue
        for c in username:
            if not c.isalnum():
                if c not in ('-', '_'):
                    valid_name = False
                    break
        if valid_name:
            filtered.append(username)
    nl = '\n'
    return nl.join(filtered)


usernames = input().split(', ')

print(filter_usernames(usernames))
