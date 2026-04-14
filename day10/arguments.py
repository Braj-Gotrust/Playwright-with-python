# Argument types -> 1. Arbitrary of variable-length argument
                #   2. Positional and required arguments
                #   3. Keyword arguments
# Approach 1 -> Arbitrary of variable-length argument
def sum(a,b,c):
    return a+b+c
print(sum(1,2,3))  # this approach is not good

def sum1(*number):   # *number can be take multiple parameter value one by one
    total = 0
    for i in number:
        total += i
    return total
print(sum1(10,20,20)) # this approach is well
print(sum1(1,200))
print(sum1(30))
print(sum1(10,20,20,50,100,300,500,1000,200))

# Approach 2 & 3 -> positional argument and keyword argument

def myfun(i,j):
    print(i,j)
myfun(10,20) # It's positional argument , it does follow order
myfun(j=40,i=30) # It's keyword arguments , do not followed order





