a="Braj"
b='kishor'
c='This is a my book'
print(a)
print(b)
print(c)

d=str("welcome")
print(d)

e=str(a)
print(e)

print(d[1:4])
print(d[:4])
print(d[3:])
print(d[1:-2])
print(d[-1:-4])

# concatenation
str1="helo braj"
str2='hi suraj'
age=25
print(str1+str2)

#print("simultaneously"+ age)  It is a typeError

print("My name is braj and my age is "+str(age))

# formating
print( f"My name is braj and my age is {age} ")
data= f"this is for you and your age {age}"
print(data)

price=1531.000
s1= f"the price is {price:.2f}"
s2= f"the price is {price:.4f}"
s3= f"the price is {price * 2}"

print(s1)
print(s2)
print(s3)

# 'in' operator

abc="welcome"
print("come" in abc) #true
print('lco' in abc) #true
print('lome' not in abc) #true
print('lcome' not in abc) #false    




