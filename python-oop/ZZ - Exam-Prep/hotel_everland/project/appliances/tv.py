from project.appliances.appliance import Appliance


class TV(Appliance):
    _default_cost = 1.5

    def __init__(self) -> None:
        super().__init__(self._default_cost)