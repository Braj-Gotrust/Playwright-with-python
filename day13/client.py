print("First approach : ")
import operations  # Entire module import
import category

# first module methods
operations.add(3,4)
operations.mul(3,4)
print("This is a client window : ",operations.mylist[3])
print(operations.mydict1["name"])

# second module method
category.add(5,6)
category.fun1()



print("second approach : ")

from operations import add,mul,mylist,mydict1  # Mentions method only import
add(10,20)
mul(10,20)
print(mylist[1])
print(mydict1["age"])

from category import fun1,add
add(100,300)
fun1()


print("Third approach : ")

from operations import *  # Entire method import not module
add(100,20)
mul(10,50)
print(mylist[3])
print(mydict1["age"])

from category import *
add(1000,3000)
fun1()
