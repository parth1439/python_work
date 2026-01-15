# 14) Write a Python program to show multilevel inheritance.

class grandparents:
    def show_granparents(self):
        print("This is grandparents class")

class parents(grandparents):
    def show_parents(self):
        print("This is parents class")

class child(parents):
    def show_child(self):
        print("This is child class")

c1=child()

c1.show_granparents()
c1.show_parents()
c1.show_child()
