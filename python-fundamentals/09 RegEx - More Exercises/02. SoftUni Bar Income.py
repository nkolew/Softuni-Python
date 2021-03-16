import re


cust_pattern = r'(?<=\%)([A-Z][a-z]+)(?=\%)'
prod_pattern = r'(?<=\<)([\w]+)(?=\>)'
count_pattern = r'(?<=\|)([\d]+)(?=\|)'
price_pattern = r'([\d]+(\.[\d]+)?)(?=\$)'
income = 0
while True:
    data = input()
    if data == 'end of shift':
        break
    m_cust = re.search(cust_pattern, data)
    m_prod = re.search(prod_pattern, data)
    m_count = re.search(count_pattern, data)
    m_price = re.search(price_pattern, data)
    if m_cust and m_prod and m_count and m_price:
        customer = m_cust.group()
        product = m_prod.group()
        count = int(m_count.group())
        price = float(m_price.group())
    else:
        continue
    total=count*price
    print(f'{customer}: {product} - {total:.2f}')
    income += total

print(f'Total income: {income:.2f}')
