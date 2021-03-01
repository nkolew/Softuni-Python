num = float(input())

while not 1 <= num <= 100:
    num = float(input())

print(f'The number {num} is between 1 and 100')


num = float(input())

while num > 100 or num < 1:
    num = float(input())

print(f'The number {num} is between 1 and 100')
