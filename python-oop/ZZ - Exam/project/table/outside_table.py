from typing import ClassVar

from project import Table


class OutsideTable(Table):
    _valid_numbers_range: ClassVar[range] = range(51, 101)
    _invalid_number_message: ClassVar[str] = "Outside table's number must be between 51 and 100 inclusive!"
