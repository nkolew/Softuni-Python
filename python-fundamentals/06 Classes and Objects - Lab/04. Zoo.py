class Animal:
    def __init__(self, species, kind) -> None:
        self.species = species
        self.kind = kind


class Zoo:
    __animals = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def filter_species(self, species):
        animals = []
        group = ''
        if species == 'mammal':
            animals = self.mammals
            group = 'Mammals'
        elif species == 'fish':
            animals = self.fish
            group = 'Fishes'
        elif species == 'bird':
            animals = self.birds
            group = 'Birds'
        return (animals, group)

    def add_animal(self, animal: Animal):
        species = animal.species
        animals, group = self.filter_species(species)
        animals.append(animal)
        Zoo.__animals += 1

    def get_info(self, species: str):
        animals, group = self.filter_species(species)
        return (
            f'{group} in {self.name}: {", ".join([e.kind for e in animals])} \
            \nTotal animals: {Zoo.__animals}'
        )


zoo_name: str = input()
z = Zoo(zoo_name)
n: int = int(input())

for _ in range(n):
    species, kind = input().split()
    z.add_animal(Animal(species, kind))

species: str = input()

print(z.get_info(species))
