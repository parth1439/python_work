# 13) Write a Python program to show single inheritance. 

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):    
    def bark(self):
        print("Dog can bark")

d1=Dog()
d1.eat()
d1.bark()
