# set is a mutable, It can be change
# set is allowed duplicate value
# set is stored data in un-ordered because set is not support indexing
# set is contain value {}

# set is same worked as a list and tuple

set1={"braj",True,3,"suraj"}
print(set1)

# Count() is not allowed because Set is not contain duplicate value
# sort() is not allowed because set is store value in un-ordered
# reverse() is not allowed

set1.add("tulsi") # add() - add single value
set1.add("chetan")
print(set1)

set1.update(["aman", "john","sarika"])  # update()- add multiple value
print(set1)

set2={1,2,3,4,5,6,"aman"}
print(set2)

set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)