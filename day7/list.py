# String is Immutable (It can not be change)
# List is Mutable (It can be change)

mylist=[1,2,3,"Braj",True,"Braj123","A"]
print(mylist)
print(mylist[0])
print(mylist[3])
print(mylist[-1])
print(mylist[2:6])
print(mylist[:2])
print(mylist[2:])
print(mylist[2:-3])

print(mylist)
print(id(mylist)) #Address of the memory

mylist[2]="suraj"
print(mylist)

print(id(mylist)) #Address of the memory

print("for loop in list")
for i in mylist:
    print(i)

if "suraj" in mylist:
    print(" Yes, suraj is in list")
else:
    print(" NO, suraj is not in list")


print(len(mylist))

list1=[3,6,8,9,5,4,3,5,3,5,3,3]
print(len(list1))
print(list1.count(3))


# Shorting
list2=[3,6,8,9,5,4,3,5,3,5,3,3]
print(list2)
list2.sort() # data is present ascending order
print(list2)
list2.sort(reverse=True) # data is present descending order
print(list2)
list2.reverse()
print(list2)
list2.append(27) # add the value end of the list
print(list2)
list2.insert(2,"suraj")
print(list2)
list2.remove(27) # remove the value
print(list2)
list2.pop(2) # index number
print(list2)
list2.append("aman")
print(list2)
del list2[12] # index number
print(list2)
del list2 # entire list2 delete

# copy list
list3=[3,6,8,9,5,4,3,5,3,5,3,3]
list4=list3.copy()
print(list3)
print(list4)

list3=list(list3) # copy data
print(list3)
 # copying
list5=["suraj","braj","tulsi"]
list6=[4,3,6,8]
for i in list5:
    list6.append(i)
print(list6)

# copy with extend()
list5=["suraj","braj","tulsi"]
list6=[4,3,6,8]
list5.extend(list6)
print(list5)

