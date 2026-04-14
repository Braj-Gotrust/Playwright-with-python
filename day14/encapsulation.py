# Encapsulation means to contain the methods,functions,variables into the single unit like class
# It can be use the access data from 'setter' & 'getter' methods

class Student:
    def __init__(self, name):
        self.name = name  # This type of variable is default public
        self.__marks=0    # This variable is private, to represent in underscore '__'

    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks, Please enter 0 to 100 : ")

    def get_marks(self):
        return self.__marks,self.name

obj1=Student("John")
obj1.set_marks(90)
print(obj1.get_marks())