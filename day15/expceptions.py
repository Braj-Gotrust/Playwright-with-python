# try:
#     num=int(input("Enter a number: "))
#     result=100/num
#     print(result)
# except ZeroDivisionError:
#     print("Division by zero")
# except ValueError:
#     print("Please enter a valid number")
# else:   # only try block will run then else block run
#     print("This is a 'else' block")
#     print(result)
# finally:   # Always run
#     print("This is the 'finally' block")






# raise Exception() -> It will work as a throws keyword but in python use raise keyword
x=3
if not type(x) is int:
    raise TypeError("Only integers are allowed")
else:
    print(x)


# How the developer raise exception
def set(age):
    if age<0:
        raise TypeError("Age must be positive number")
    print("Age is set : ",age)

# set(20)  # valid data
# set(-20) # invalid data
try:
    set(20)
except ValueError:
    print("Invalid age data")










