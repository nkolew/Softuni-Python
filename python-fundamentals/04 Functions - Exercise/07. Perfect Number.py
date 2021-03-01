def perfect_num_chk(n):

    perfect = True
    divisors = [div for div in range(1, n) if n % div == 0]

    if n != sum(divisors):
        perfect = False

    if not perfect:
        return "It's not so perfect."

    return 'We have a perfect number!'


number = int(input())

print(perfect_num_chk(number))
