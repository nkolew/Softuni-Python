class Catalogue:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products: list = []

    def add_product(self, product: str):
        self.products.append(product)

    def get_by_letter(self, first_letter: str):
        return [p for p in self.products if p[0] == first_letter]

    def __repr__(self) -> str:
        nl = '\n'
        return (
            f'Items in the {self.name} catalogue:{nl}{nl.join(sorted(self.products))}'
        )


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
