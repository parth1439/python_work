# 15) Write a Python program to show multiple inheritance

class Father:
    def show_Father(self):
        print("This is Father class")

class Mother:
    def show_Mother(self):
        print("This is Mother class")

class Child(Father,Mother):
    def show_child(self):
        print("This is child class")

c1=Child()

c1.show_Father()
c1.show_Mother()
c1.show_child()