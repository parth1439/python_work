# 16) Write a Python program to show hierarchical inheritance.

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("dog can bark")

class cat(Animal):
    def meow(self):
        print("cat can meow")

d1=Dog()
c1=cat()

d1.eat()
d1.bark()

c1.eat()
c1.meow()