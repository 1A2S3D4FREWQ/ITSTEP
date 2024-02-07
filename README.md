class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass 

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name} - {animal.species}")

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"


zoo = Zoo()
lion = Lion("Leo", "Lion")
elephant = Elephant("Dumbo", "Elephant")


zoo.add_animal(lion)
zoo.add_animal(elephant)


zoo.display_animals()


for animal in zoo.animals:
    print(f"{animal.name} says: {animal.make_sound()}")
