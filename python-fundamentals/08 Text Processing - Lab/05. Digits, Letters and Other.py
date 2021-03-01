string = input()

nums = ''
lets = ''
others = ''

for c in string:
    if c.isdigit():
        nums += c
    elif c.isalpha():
        lets += c
    else:
        others += c

print(nums)
print(lets)
print(others)
