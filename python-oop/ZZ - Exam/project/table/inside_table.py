from typing import ClassVar

from project import Table


class InsideTable(Table):
    _valid_numbers_range: ClassVar[range] = range(1, 51)
    _invalid_number_message: ClassVar[str] = "Inside table's number must be between 1 and 50 inclusive!"
