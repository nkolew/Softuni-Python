class Vet:
    animals = []
    space = 5

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space <= 0:
            return 'Not enough space'

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        Vet.space -= 1
        return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name not in Vet.animals:
            return f'{animal_name} not in the clinic'

        self.animals.pop(self.animals.index(animal_name))
        Vet.animals.pop(Vet.animals.index(animal_name))
        Vet.space += 1
        return f'{animal_name} not in the clinic'

    def info(self) -> str:
        return f'{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic'


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
