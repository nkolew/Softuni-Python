def palindrome_chk(numlist):

    return [True if (num == num[::-1]) else False for num in numlist.split(', ')]


num_list = input()

for line in palindrome_chk(num_list):
    print(line)
