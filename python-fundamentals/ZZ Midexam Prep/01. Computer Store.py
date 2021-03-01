class ComputerPart:
    def __init__(self, price: float) -> None:
        self.price = price
        self.tax = 0.2 * self.price
        self.total = self.price + self.tax


class StoreReceipt:
    def __init__(self) -> None:
        self.parts = []
        self.prices = 0
        self.taxes = 0
        self.total = 0
        self.special = False

    def add_part(self, part: ComputerPart):
        if part.price < 0:
            print("Invalid price!")
        else:
            self.parts.append(part)

    def set_special(self):
        self.special = True

    def calc_prices(self):
        self.prices = sum([part.price for part in self.parts])
        self.taxes = sum([part.tax for part in self.parts])
        self.total = sum([part.total for part in self.parts])

        if self.special:
            self.total *= 0.9

    def __repr__(self) -> str:
        if self.total == 0:
            return 'Invalid order!'

        return (
            f"Congratulations you've just bought a new computer!"
            "\n"
            f"Price without taxes: {self.prices:.2f}$"
            "\n"
            f"Taxes: {self.taxes:.2f}$"
            "\n"
            "-----------"
            "\n"
            f"Total price: {self.total:.2f}$"
        )


receipt = StoreReceipt()

while True:
    tokens = input()
    if tokens == 'special':
        receipt.set_special()
        receipt.calc_prices()
        break
    if tokens == 'regular':
        receipt.calc_prices()
        break
    part_price = float(tokens)
    part = ComputerPart(part_price)
    receipt.add_part(part)

print(receipt)
