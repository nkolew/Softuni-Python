from project.appliances.appliance import Appliance


class Laptop(Appliance):
    _default_cost = 1.0

    def __init__(self) -> None:
        super().__init__(self._default_cost)