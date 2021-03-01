while True:
    string = input()
    if string == 'end':
        break
    print(f'{string} = {string[::-1]}')
