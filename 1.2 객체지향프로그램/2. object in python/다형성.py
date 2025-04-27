class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
    

class Cat(Animal):
    def talk(self):
        return "Meow!"


class Dog(Animal):
    def talk(self):
        return "woof Woof!"


animals = [Cat('Missy'), Cat("Mr. mistoeefse"), Dog("sdfw")]

for animal in animals:
    print(animal.name + ': ' + animal.talk())
