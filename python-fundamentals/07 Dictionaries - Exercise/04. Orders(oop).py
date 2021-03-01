class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class Orders:
    def __init__(self) -> None:
        self.orderlist = []

    def add_product(self, product: Product):
        product_is_new = True
        for p in self.orderlist:
            if product.name == p.name:
                product_is_new = False
                p.quantity += product.quantity
                if p.price != product.price:
                    p.price = product.price
           
        if product_is_new:
            self.orderlist.append(product)

    def __repr__(self) -> str:
        result = []
        for product in self.orderlist:
            total = product.price * product.quantity
            result.append(f'{product.name} -> {total:.2f}')
        result = '\n'.join(result)
        return result


o = Orders()

while True:
    tokens = input()
    if tokens == 'buy':
        break
    name, price, quantity = tokens.split()
    price = float(price)
    quantity = int(quantity)
    o.add_product(Product(name, price, quantity))

print(o)
