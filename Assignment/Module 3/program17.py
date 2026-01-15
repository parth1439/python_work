#17) Write a Python program to show hybrid inheritance.

class A:
    def show_A(self):
        print("A calling")

class B(A): 
    def show_B(self):
        print("B calling")

class C(A):
    def show_c(self):
        print("c calling")

class D(B,C):
    def show_d(self):
        print("D calling")

c1=D()
c1.show_A()
c1.show_B()
c1.show_c()
c1.show_d()



    