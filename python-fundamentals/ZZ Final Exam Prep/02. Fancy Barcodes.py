import re


pattern = r'(?:(^@#+)(?P<code>[A-Z][A-Za-z0-9]{4,}[A-Z])(@#+$))'
nums_pattern = r'\d'

n = int(input())
for _ in range(n):
    data = input()
    m = re.fullmatch(pattern, data)
    if not m:
        print('Invalid barcode')
        continue
    code = m.group('code')
    nums = re.findall(nums_pattern, code)
    product_group = '00'
    if len(nums) != 0:
        product_group = ''.join(nums)
    print(f'Product group: {product_group}')
