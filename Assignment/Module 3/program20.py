#  20) Write a Python program to show method overriding.


class parent:
    def show(self):
        print("This is parent class")

class child:
    def show(self):
        print("This is child class")

c1=child()
c1.show()