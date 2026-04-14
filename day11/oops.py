# create a class inside the methods

class Myclass:
    def myfunc(self):  # 'self' does not parameter of the myfunc method
        pass   # It is a empty methods  to represent 'pass' keyword

    def myfunc2(self,name):  # this method 'self' keyword does not consider as parameter,but 'name' is parameter
        print(name)

    @staticmethod
    def myfunc3(self,num): # In case method is static to 'self' keyword consider as a parameter
        print(self,num)

Myclass().myfunc()
Myclass().myfunc2("braj")

m1=Myclass()
m1.myfunc()
m1.myfunc2("suraj")

m1.myfunc3(3,8)


print("Variable of the class and method")

class Myclass1:
    a,b=10,20
    def add(self):
        print(self.a+self.b)  # Do not access global variable inside the class without the self keyword
    def mul(self):
        print(self.a*self.b)
Myclass1().add()
Myclass1().mul()








