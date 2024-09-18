class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        pass

class Swim:
    def sw(cls):
        return 'blop-blop'

class Fly:
    def fl(cls):
        return 'Its a birdie? Its an airplane?'

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Duck(Animal, Swim, Fly):
    def make_sound(self):
        return 'Quak!'

dog = Dog("Canine")
cat = Cat("Feline")
duck = Duck('Ducke')

print(dog.make_sound())  # Bark!
print(cat.make_sound())  # Meow!
print(duck.fl())
print(duck.species)