from typing import List, Optional

from project import BakedFood, Drink, Table, Bread, Cake, Tea, Water, OutsideTable, InsideTable


class Bakery:
    _name: str
    food_menu: List[BakedFood]
    drinks_menu: List[Drink]
    tables_repository: List[Table]
    total_income: float

    def __init__(self, name: str) -> None:
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError('Name cannot be empty string or white space!')
        self._name = value

    def add_food(self, food_type: str, name: str, price: float) -> Optional[str]:
        '''
        Creates a food with the correct type and adds it to the menu. The possible types of food are "Bread" and "Cake". If the food is created and added successfully, returns:
        "Added {baked_food_name} ({baked_food_type}) to the food menu"
        If a baked food with the given name already exists in the food menu, raise an Exception with message "{food_type} {name} is already in the menu!"
        '''
        food_types = {
            'Bread': Bread,
            'Cake': Cake,
        }
        # try/except?
        food = food_types[food_type](name, price)

        if food in self.food_menu:
            raise Exception(f'{food_type} {name} is already in the menu!')

        self.food_menu.append(food)
        return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str) -> Optional[str]:
        '''
        Creates a drink with the correct type and adds it to the menu. The possible types of drinks are "Tea" and "Water".  If the drink is created and added successfully, returns:
        "Added {drink_name} ({drink_brand}) to the drink menu"
        If a drink with the given name already exists in the drink repository, raise Exception with message "{drink_type} {name} is already in the menu!"
        '''
        drink_types = {
            'Tea': Tea,
            'Water': Water,
        }

        drink = drink_types[drink_type](name, portion, brand)

        if drink in self.drinks_menu:
            raise Exception(f'{drink_type} {name} is already in the menu!')

        self.drinks_menu.append(drink)
        return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        '''
        Creates a table with the correct type, adds it to the table respository. The possible types of tables are "InsideTable" and "OutsideTable".  If the table is created and added successfully, returns:
        "Added table number {table_number} in the bakery"
        If a table with the given number already exists in the table repository, raise Exception with message "Table {table_number} is already in the bakery!"
        '''
        table_types = {
            'InsideTable': InsideTable,
            'OutsideTable': OutsideTable,
        }

        table = table_types[table_type](table_number, capacity)

        if table in self.tables_repository:
            raise Exception(f'Table {table_number} is already in the bakery!')

        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    def _find_suitable_table(self, number_of_people: int) -> Optional[Table]:
        for t in self.tables_repository:
            if t.is_reserved or t.capacity < number_of_people:
                continue
            return t
        return None

    def _find_table_by_number(self, table_number: int) -> Optional[Table]:
        for t in self.tables_repository:
            if not t.table_number == table_number:
                continue
            return t
        return None

    def reserve_table(self, number_of_people: int) -> str:
        '''
        Finds the first possible table which is not reserved, and its capacity is enough for the number of people provided. Then reserves the table and returns:
        "Table {table_number} has been reserved for {number_of_people} people"
        Otherwise, returns:
        "No available table for {number_of_people} people"
        '''

        table = self._find_suitable_table(number_of_people)

        if not table:
            return f'No available table for {number_of_people} people'

        table.reserve(number_of_people)
        return f'Table {table.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number: int, *food_names):
        '''
        The order_food method will receive a table's number and different number of strings with food's names.
        Finds the table with that number. If there is no such table returns:
        "Could not find table {table_number}"
        Otherwise, adds the food which could be ordered (are in the menu) in the table's orders, returns the information about the ordered food and the food that is not in the menu in the format:
        "Table {table_number} ordered:
        - {baked_food_name1}: {portion1}g - {price1}lv
        - {baked_food_name2}: {portion2}g - {price2}lv
        ...
        - {baked_food_nameN}: {portionN}g - {priceN}lv
        {bakery_name} does not have in the menu:
        {food_name_not_in_the_menu1}
        {food_name_not_in_the_menu2}
        ...
        {food_name_not_in_the_menuN}"
        '''
        table = self._find_table_by_number(table_number)
        if not table:
            return f'Could not find table {table_number}'

        msg = [f'Table {table_number} ordered:']

        foods = [f.name for f in self.food_menu]

        for food_name in food_names:
            for f in self.food_menu:
                if f.name == food_name:
                    self.total_income += f.price
                    msg.append(
                        f'- {f.name}: {f.portion}g - {f.price}lv')
        for food in food_names:
            if food not in foods:
                msg.append(f'{food}')

        return '\n'.join(msg)

    def order_drink(self, table_number: int, *drink_names) -> str:
        '''
        The order_drink method will receive a table's number and different number of strings with drink's names.
        Finds the table with that number. If there is no such table, it returns:
        "Could not find table {table_number}"
        Otherwise, adds the drinks which could be ordered (are in the menu) in the table's orders, returns orders of the drinks which are in the menu and the ones that are not:
        "Table {table_number} ordered:
        - {drink_name1} {brand_name1} - {portion1}ml - {price1}lv
        - {drink_name2} {brand_name2} - {portion2}ml - {price2}lv
        ...
        - {drink_nameN} {brand_nameN} - {portionN}ml - {priceN}lv
        {bakery_name} does not have in the menu:
        {drink_name_not_in_the_menu1}
        {drink_name_not_in_the_menu2}
        ...
        {drink_name_not_in_the_menuN}"
        '''
        table = self._find_table_by_number(table_number)
        if not table:
            return f'Could not find table {table_number}'

        msg = [f'Table {table_number} ordered:']

        drinks = [d.name for d in self.drinks_menu]

        for drink_name in drink_names:
            for d in self.drinks_menu:
                if d.name == drink_name:
                    self.total_income += d.price
                    msg.append(
                        f'- {d.name} {d.brand} - {d.portion}ml - {d.price}lv')
        for drink in drink_names:
            if drink not in drinks:
                msg.append(f'{drink}')

        return '\n'.join(msg)

    def leave_table(self, table_number: int) -> Optional[str]:
        '''
        Finds the table with the same table number. Gets the bill for that table and clears it. Finally returns:
        "Table: {table_number}"
        "Bill: {table_bill}"
        The bill price should be formatted to the second decimal point.
        '''
        bill = None
        table = self._find_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            table.clear()
            return f'''Table: {table_number}
        Bill: {bill:.2f}'''

    def get_free_tables_info(self):
        '''For each free table returns the table info. Each table info should start on a new row.'''
        msg = []
        for t in self.tables_repository:
            if not t.is_reserved:
                msg.append(t.free_table_info())
        return '\n'.join(msg)

    def get_total_income(self):
        '''
        Returns the total income in the format, formatted to the second decimal point:
        "Total income: {income}lv"
        '''
        return f'Total income: {self.total_income}lv'
