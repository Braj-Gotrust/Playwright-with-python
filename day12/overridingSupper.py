class A:
    def m1(self):
        print("this is m1 method")

class B(A):   # single inheritance
    def m1(self):  # override method
        print("this is m2 method")

class C(B): # multilevel inheritance
    def m1(self):  # override method
        print("this is m3 method")
        super().m1()   # invoke the immediate parent class method, not a parent of super class

c_obj = C()
c_obj.m1()