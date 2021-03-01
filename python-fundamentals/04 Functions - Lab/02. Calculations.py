def calc(o,n1,n2):
    result = None
    
    if o == 'multiply':
        result = n1 * n2

    elif o == 'divide' and n2 != 0:
        result = n1 // n2

    elif o == 'add':
        result = n1 + n2

    elif o == 'subtract':
        result = n1 - n2

    return result


operator = input()
number_1 = int(input())
number_2 = int(input())

print(calc(operator,number_1,number_2))