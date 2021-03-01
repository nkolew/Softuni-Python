class Inventory:
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self) -> str:
        return f'Items: {", ".join([e for e in self.items])}.\nCapacity left: {self.__capacity - len(self.items)}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
