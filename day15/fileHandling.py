# # approach 1
# file=open("/home/user/Desktop/Automation/automationFiles/file1.txt","w")
# file.write("hello BRAJ\nWhat are you doing")
# file.close()

# # approach 2 -> using 'with' keyword
# with open("/home/user/Desktop/Automation/automationFiles/file2.txt","w") as file:
#     file.write("hello BRAJ\nWhat are you doing")
#     file.close()
#
# # append()-> This method to use  add some data of the file
# file=open("/home/user/Desktop/Automation/automationFiles/file2.txt","a")
# file.write("hello BRAJ\nThis is a append method")
# file.close()


file=open("/home/user/Desktop/Automation/automationFiles/file1.txt","r")
# content=file.read() # All line text data read
# content=file.readline() # only one line text data read
content=file.readlines() # All line text data read in list format

print(content)

file.close()

# # file rename
# import os
# os.rename("/home/user/Desktop/Automation/automationFiles/file3.txt","/home/user/Desktop/Automation/automationFiles/braj.txt")
# print("file rename successfully")
# file.close()

# Deleting the file
import os
file = "/home/user/Desktop/Automation/automationFiles/braj.txt"
if os.path.exists(file):
    os.remove(file)
    print("File successfully removed")
else:
    print("File does not exist")

