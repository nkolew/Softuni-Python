number = int(input())

number_is_prime = True

for div in range(2, number):
    if number % div == 0:
        number_is_prime = False
        break

print(number_is_prime)
