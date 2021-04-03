import re


pattern = r'(?P<us>U\$)(?P<u>[A-Z][a-z]{2,})(?P=us)(?P<ps>P@\$)(?P<p>[A-Za-z]{5,}[0-9]{1,})(?P=ps)'

n = int(input())
reg_count = 0

for _ in range(n):
    s = input()
    m = re.fullmatch(pattern, s)
    if m is not None:
        reg_count += 1
        username = m['u']
        password = m['p']
        print('Registration was successful')
        print(f'Username: {username}, Password: {password}')
    else:
        print('Invalid username or password')

print(f'Successful registrations: {reg_count}')
