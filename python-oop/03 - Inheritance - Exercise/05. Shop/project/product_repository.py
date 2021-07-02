from typing import List, Optional

from project import Product


class ProductRepository:
    products: List[Product]

    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str) -> None:
        for i, p in enumerate(self.products):
            if p.name == product_name:
                self.products.pop(i)
                return

    def __repr__(self) -> str:
        message = []
        NL = '\n'

        for p in self.products:
            message.append(str(p))

        return NL.join(message)
