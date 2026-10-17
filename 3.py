class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
dog = Dog()
dog.eat()
dog.bark()

class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
