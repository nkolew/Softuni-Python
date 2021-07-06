class Integer:
    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):

        if not isinstance(float_value, float):
            return f'value is not a float'

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        ROMAN_DIGITS = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in ROMAN_DIGITS:
                num += ROMAN_DIGITS[value[i:i + 2]]
                i += 2
            else:
                num += ROMAN_DIGITS[value[i]]
                i += 1

        return cls(num)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return 'wrong type'
        
        try:
            int_value = int(value)
            return cls(int_value)

        except ValueError:
            return f'wrong type'

    def __repr__(self) -> str:
        return f'{self.value}'


first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(first_num)
print(second_num)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
