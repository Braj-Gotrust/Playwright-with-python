#approach 1
Name = "Braj"
Age = 25
Salary = 50000.40
print("Name:",Name)
print("Age:",Age)
print("Salary:",Salary)

#approach 2
name,age,salary="braj",26,60000.50
print("All details:",name,age,salary)

#approach 3
# %s for string
# %d for integers
# %g for floats
print("Name:%s \n Age:%d \n Salary:%g" %(name,age,salary))

#approach 4
print("Name\tis :{}, Age\tis :{}, Salary\tis :{}".format(name,age,salary))  # tab space
print("{},{},{}".format(name,age,salary))

#approach 5
print("Name is :{0}, Age is :{1}, Salary is :{2}".format(name,age,salary))
print("Age is :{1}, \nName is :{0}, \nSalary is :{2}".format(name,age,salary))
