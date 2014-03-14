class Animal(object): pass

class Dog(Animal):
    def noise(self):
        return "Bark"

class Cat(Animal):
    def noise(self):
        return "Miaow"

class Pig(Animal):
    def noise(self):
        return "Oink"

class Cow(Animal):
    def noise(self):
        return "Moo"

animals=[Dog(), Dog(), Cat(), Pig(), Cow(), Cat()]
for animal in animals:
    print animal.noise()

