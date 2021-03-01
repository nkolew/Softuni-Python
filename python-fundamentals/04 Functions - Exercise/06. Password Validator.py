def passwd_chk(passwd):

    LEN_RANGE = range(6, 11)
    MIN_DIG_COUNT = 2

    e1 = 0
    e2 = 0
    e3 = 0

    dig_counts = 0
    valid = True

    if len(passwd) not in LEN_RANGE:
        valid = False
        e1 += 1

    for c in passwd:
        if c.isnumeric():
            dig_counts += 1

        if not c.isalnum():
            valid = False
            e2 += 1

    if dig_counts < MIN_DIG_COUNT:
        valid = False
        e3 += 1

    if valid:
        return 'Password is valid'

    else:
        if e1 > 0 and e2 > 0 and e3 > 0:
            return "Password must be between 6 and 10 characters \nPassword must consist only of letters and digits \nPassword must have at least 2 digits"
        elif e1 > 0 and e2 > 0 and e3 == 0:
            return "Password must be between 6 and 10 characters \nPassword must consist only of letters and digits"
        elif e1 > 0 and e2 == 0 and e3 == 0:
            return "Password must be between 6 and 10 characters"
        elif e1 == 0 and e2 > 0 and e3 > 0:
            return "Password must consist only of letters and digits \nPassword must have at least 2 digits"
        elif e1 == 0 and e2 > 0 and e3 == 0:
            return "Password must consist only of letters and digits"
        elif e1 > 0 and e2 == 0 and e3 > 0:
            return "Password must be between 6 and 10 characters \nPassword must have at least 2 digits"
        elif e1 == 0 and e2 == 0 and e3 > 0:
            return "Password must have at least 2 digits"


password = input()

print(passwd_chk(password))
