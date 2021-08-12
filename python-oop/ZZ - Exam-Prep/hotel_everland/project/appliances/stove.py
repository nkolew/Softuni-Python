from project.appliances.appliance import Appliance


class Stove(Appliance):
    _default_cost = 0.7

    def __init__(self) -> None:
        super().__init__(self._default_cost)