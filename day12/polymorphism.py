# overloading

#Example- 1
class A:
    def m1(self,name=None):
        if name is not None:
            print("hey "+name)
        else:
            print("hey ")

obj = A()
obj.m1()
obj.m1("john")

# Example - 2
class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

obj = calculation()
#obj.add(1,2) # It can not be execute because no.of parameter different
obj.add(3,4,5)
obj.add(3,40)
obj.add(40)
obj.add()




