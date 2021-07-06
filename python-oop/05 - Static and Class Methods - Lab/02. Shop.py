from typing import Dict


class Shop:
    name: str
    type: str
    capacity: int
    items: Dict[str, int]

    def __init__(self, name: str, type: str, capacity: int) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        CAPACITY = 10
        return cls(name, type, CAPACITY)

    def add_item(self, item_name: str) -> str:
        if sum(self.items.values()) >= self.capacity:
            return 'Not enough capacity in the shop'

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f'{item_name} added to the shop'

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name not in self.items or \
                self.items[item_name] < amount:
            return f'Cannot remove {amount} {item_name}'

        self.items[item_name] -= amount
        return f'{amount} {item_name} removed from the shop'

    def __repr__(self) -> str:
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
