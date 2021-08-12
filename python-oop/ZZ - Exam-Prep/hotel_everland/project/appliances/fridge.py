from project.appliances.appliance import Appliance


class Fridge(Appliance):
    _default_cost = 1.2

    def __init__(self) -> None:
        super().__init__(self._default_cost)