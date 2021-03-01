from collections import defaultdict


class Employee:
    def __init__(self, id: str) -> None:
        self.id = id


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def __existsencecheck__(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return True
        return False

    def add_employee(self, employee: Employee):
        if not self.__existsencecheck__(employee.id):
            self.employees.append(employee)


class Inventory:
    def __init__(self) -> None:
        self.companies = defaultdict(list)

    def __exists__(self, company_name: str):
        return company_name in self.companies

    def add_company(self, company_name, employee_id):
        e = Employee(employee_id)
        if not self.__exists__(company_name):
            c = Company(company_name)
            c.add_employee(e)
            self.companies[company_name].append(c)
        else:
            self.companies[company_name][0].add_employee(e)

    def __repr__(self) -> str:

        def sort_companies(data: list):
            company = data[0]
            return company.name

        result = []
        nl = '\n'
        for data in sorted(self.companies.values(), key=sort_companies):
            company = data[0]
            result.append(company.name)
            for employee in company.employees:
                result.append(f'-- {employee.id}')
        return nl.join(result)


inv = Inventory()

while True:
    tokens = input()
    if tokens == 'End':
        break
    company_name, employee_id = tokens.split(' -> ')
    inv.add_company(company_name, employee_id)

print(inv)
