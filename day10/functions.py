# function to define a 'def' keyword

# create a function
def myfunc():
    print("hello braj")

# calling/invoking the function
myfunc()

# Function with parameter but no return value
def myfunc2(name):
    print("hello " + name)
myfunc2("suraj") # passing a argument
myfunc2("rakesh") # passing a argument

# function with parameter with return value
def calc(num1,num2):
    return num1+num2
c=calc(1,2)
print(c)

def f1():
    i=100
    return i
print(f1())

