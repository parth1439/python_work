#18) Write a Python program to demonstrate the use of super() in inheritance.

class person:
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print("name:",self.name)

class student(person):          
    def __init__(self, name,roll_no):
        super().__init__(name)
        self.roll_no=roll_no
        
    def display(self):
        super().display()
        print("roll no:",self.roll_no)

s1=student("parth",101)
s1.display()








        