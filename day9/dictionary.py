# dictionary is mutable and duplicate value are not allowed, It is ordered indexing wise

# Approach 1
mydict1={"name":"Braj","age":25}
print(mydict1)

#Approach 2 using dict() constructor
mydict2=dict(name="Braj",age=25)
print(mydict2)

# A one key can have store multiple values
mydict3={
    "name":"Braj", # duplicate keys are not allowed only values allowed
    "age":25,
    "color":["red","green","blue"],
    "name":"suraj" # It is a replace the value of the key
}
print(mydict3)
print(mydict3["color"])
print(mydict3["name"])
# print(mydict3[0])  it is not following indexing order
print(mydict3.get("name"))  # using get() method to access the values

print(mydict3.keys()) # display all the key in list form
print(mydict3.values()) # display all the value in list form

print(mydict3.items())

mydict3.update({"name":"Rahul","age":29})
print(mydict3)

mydict3.pop("name")
print(mydict3)

mydict3.popitem() # last data delete
print(mydict3)

# Delete the data from the dictionary there are 4 approach -> pop(), popitem(), del(), clear()

# copy dictionary
mydict4=mydict3.copy()  # copy with copy()
print(mydict3)
print(mydict4)

mydict5=dict(mydict4) # copy with dict()
print(mydict4)
print(mydict5)

mydict5.update({"name":"Rahul","country":"india"})
print(mydict5)

for i in mydict5:  # by default print key only
    print(i)


for i in mydict5.keys(): print(i)  # print key only

for i in mydict5.values(): print(i)  # print value only

for i in mydict5:
    print(mydict5[i])  # print value only

for i in mydict5.items(): print(i)  # print all key and value

for i,j in mydict5.items(): print(i,j)  # print all key and value pair

