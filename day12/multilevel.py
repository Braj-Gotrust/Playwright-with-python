class A:
    def m1(self):
        print("this is m1 method")

class B(A):   # single inheritance
    def m2(self):
        print("this is m2 method")

class C(B): # multilevel inheritance
    def m3(self):
        print("this is m3 method")

class D(C,B,A):   # multiple inheritance
    def m4(self):
        print("this is m4 method")

d_obj=D()
d_obj.m1()
d_obj.m2()
d_obj.m3()
d_obj.m4()

c_obj=C()
c_obj.m1()
c_obj.m2()
c_obj.m3()

