from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
5
    @abstractmethod
    def sound(self):
        pass


class Cow(Animal):
    def sound(self):
        return "Moo"

class Parrot(Animal):
    def sound(self):
        return "Squawk"

class Dog(Animal):
    def sound(self):
        
        
        return "Woof"

cow = Cow("Bessie", 15)
parrot = Parrot("Polly", 12)
dog = Dog("Buddy", 20)

print(cow.sound()) 
print(parrot.sound()) 
print(dog.sound())
