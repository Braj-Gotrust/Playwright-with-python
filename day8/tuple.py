# Tuple is Immutable just like string ,It is represent to ()
# list is mutable, It is represent to []

# add and remove the value - Not possible because tuple is immutable

mytuple=("braj","suraj","tulsi")
print(mytuple)
print(mytuple[1])
print(mytuple[-1])
print(mytuple[1:3])

#mytuple[0]="sonu"  # Tuple can not change because tuple immutable

# we can change converting to list
# convert tuple to list
mylist=list(mytuple)
print("Before converting :",mylist)

mylist[0]="sonu"
print("After converting: ",mylist)

# convert list to tuple
mytuple=tuple(mylist)
print(mytuple)

if "suraj" in mytuple:
    print("suraj is present")
else:
    print("suraj is not present")


print("suraj" in mytuple) #true, This statement to return boolean value true/false
