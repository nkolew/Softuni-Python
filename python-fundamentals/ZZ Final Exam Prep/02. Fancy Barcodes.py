import re


pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
digits = r'\d'
n = int(input())


for _ in range(n):
    s = input()
    m = re.fullmatch(pattern, s)
    if m:
        product_group = '00'
        current_digits = re.findall(digits, s)
        if current_digits:
            product_group = ''.join(current_digits)
        print(f'Product group: {product_group}')
    else:
        print(f"Invalid barcode")
