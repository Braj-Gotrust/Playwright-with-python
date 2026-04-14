class Myclass:
    def __init__(self):
        print("THis is constructor")

    def m1(self):
        print("this is a m1 method")

    def m2(self,a,b):
        return a+b

# Myclass()
# Myclass().m1()    #This scenario Every time constructor is calling
# print(Myclass().m2(3,5))

mc=Myclass()   # Constructor is automatically called
mc.m1()        # It is a m1 calling
print(mc.m2(3,5))  # It is m2 calling



print("Constructor with parameters and class variables")
class Myclass2:
    name="David"
    def __init__(self,name):
        print(name) # local variable
        print(self.name)  # class variable
Myclass2("scott")


print("A class with constructor and method")
class Employee:
    def __init__(self,eid,ename,esalary):
        self.eid=eid
        self.ename=ename
        self.esalary=esalary

    def display(self):
        print(self.eid,self.ename,self.esalary)

mc=Employee(101,"David",60000)
mc.display()
