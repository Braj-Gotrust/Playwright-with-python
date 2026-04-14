# delimeters - @,#,$,!,%,&,*,'space',',',(),_,;,:

s1="abc@gmail.com"  # return type string
lst=s1.split("@") # return type list
print(lst)
print(lst[0])
print(lst[1])
print(type(lst))

s2="one,two,three,four, five"
list1=s2.split(",")
print(list1)
print(list1[3])

s3="    Braj Kishor    "
print(s3.startswith("Braj")) #true  , It is a case sensitive
print(s3.startswith("braj")) #false
print(s3.endswith("kishor")) #true

# Trimming space- strip(), lstrip(), rstrip()  = l-left, r-right side space
print(s3.strip())
print(s3.rstrip())
print(s3.lstrip()) 

