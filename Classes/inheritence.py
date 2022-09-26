class Animal:

    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Fish(Animal):
    def Swim(self):
        print("swim")


class Mammal(Animal):

    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 1

    def walk(self):
        print("walk")


Elephant = Mammal()
Elephant.eat()
Elephant.walk()
print(Elephant.age)

fish = Fish()
fish.Swim()
