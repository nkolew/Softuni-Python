def datatype_check(typ, data):

    if typ == 'int':
        return int(data) * 2

    elif typ == 'real':
        return float(data) * 1.5

    elif typ == 'string':
        return f'${data}$'


typ = input()
data = input()

print(datatype_check(typ, data))