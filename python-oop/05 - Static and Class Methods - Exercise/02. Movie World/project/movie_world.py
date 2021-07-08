from typing import ClassVar, List

from project import DVD, Customer


class MovieWorld:
    name: str
    customers: List[Customer]
    dvds: List[DVD]
    _CUSTOMER_CAPACITY: ClassVar[int] = 10
    _DVD_CAPACITY: ClassVar[int] = 15

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls) -> int:
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls) -> int:
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if self.__class__._CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.__class__._DVD_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def __get_customer_by_id(self, id: int) -> Customer:
        for c in self.customers:
            if c.id == id:
                return c

    def __get_dvd_by_id(self, id: int) -> DVD:
        for d in self.dvds:
            if d.id == id:
                return d

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.__get_customer_by_id(customer_id)
        dvd = self.__get_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'

        if dvd.is_rented:
            return 'DVD is already rented'

        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self.__get_customer_by_id(customer_id)
        dvd = self.__get_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f'{customer.name} has successfully returned {dvd.name}'

        return f'{customer.name} does not have that DVD'

    def __repr__(self) -> str:
        message = []
        NL = '\n'

        for c in self.customers:
            message.append(f'{repr(c)}')

        for d in self.dvds:
            message.append(f'{repr(d)}')

        return NL.join(message)
