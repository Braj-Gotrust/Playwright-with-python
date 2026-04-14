s1="braj"
print(s1.capitalize())
print(s1.upper())
print(s1.isupper()) #false , It is return boolean value true/false
print(s1.islower()) #true, It is return boolean value true/false


s2="BRAJ"
print(s2.capitalize())
print(s2.lower())


s3="Braj"
print(s3.casefold()) # it is same work
print(s3.lower())    #it is same work

s4="my name is braj"
print(s4.title())
print(s4.capitalize())
print(s4.upper())
print(s4.lower())

print(s4.replace('braj','suraj'))


s5="This is for Suraj"
print(s5.swapcase())

s6="Braj"
print(s6.center(20))
print(s6.center(20,'*'))
print(s6.center(10,'*'))
print(s6.center(11,'*'))

# format()
s7="Johnnynn"
print("Hello {}".format(s7))
print(s7.find('h'))  # it will return index number
print(s7.find('n'))  # it will return index number
print(s7.find('b'))  # value is not found, it will return index number always -1

print(s7.index('h'))  # it will return index number
print(s7.index('n'))  # it will return index number
#print(s7.index('b'))  # Value is not found, it will return ValueError

print("Count function")
print(s7.count('n'))
print(s7.count('nn'))

print(len(s7))
print(s7.__len__())

#alphanumeric value
s8="Braj123"
print(s8.isalnum()) #ture
s9="braj!!_1"
print(s8.isalpha()) #false
s10="braj"
print(s10.isalpha()) #true
s11="1234"
print(s11.isalpha()) #false

print(s11.isdecimal()) #true

print(s11.isnumeric()) #true

