print("Global variable,Class variables and Local variables")

i,j=100,200                  # Global variables
class Myclass2:
    x,y=10,20               # Class variables
    def add(self,m,n):      # Local variables
        print(m+n)          # Local variables
        print(self.x+self.y)# Class variables
        print(i+j)          # Global variables
Myclass2().add(50,60)


print("If we have same name of Global variable,Class variables and Local variables")

c,d=100,200                  # Global variables
class Myclass2:
    c,d=10,20               # Class variables
    def add(self,c,d):      # Local variables
        print(c+d)          # Local variables
        print(self.c+self.d)# Class variables

        print(globals()['c']+globals()['d'])          # Global variables

Myclass2().add(50,60)