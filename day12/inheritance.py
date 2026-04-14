class myclass1:
    def m1(self):
        print("THis method m1")

class myclass2(myclass1):  # It is
    def m2(self):
        print("THis method m2")

obj=myclass2()
obj.m1()
obj.m2()