class DVD:
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.id == o.id

    def __hash__(self) -> int:
        return hash(self.id)

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> 'DVD':
        MONTH_BY_NUM = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December',
        }

        _, month, year = date.split('.')
        creation_year = int(year)
        creation_month = MONTH_BY_NUM[month]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self) -> str:
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {"rented" if self.is_rented else "not rented"}'
