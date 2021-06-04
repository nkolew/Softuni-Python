nums = list(map(int, input().split(', ')))

positive = (n for n in nums if n >= 0)
negative = (n for n in nums if n < 0)
even = (n for n in nums if n % 2 == 0)
odd = (n for n in nums if n % 2 != 0)

print(f'Positive: {", ".join(str(n) for n in positive)}')
print(f'Negative: {", ".join(str(n) for n in negative)}')
print(f'Even: {", ".join(str(n) for n in even)}')
print(f'Odd: {", ".join(str(n) for n in odd)}')
