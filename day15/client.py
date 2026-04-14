# import fileOperationsFunctions
# from day15.fileOperationsFunctions import *
from traceback import print_tb

import fileOperationsFunctions as fo

path = "/home/user/Desktop/Automation/automationFiles/file123.txt"
fo.write_to_file(path,"hey mr. Boss, dont talk to me")

# append to file
fo.append_to_file(path,"\nhey buddy I am good ")

# Read file
print(fo.read_file(path,"all"))

# Rename file
fo.read_file(path,"/home/user/Desktop/Automation/automationFiles/Braj.txt")

# file delete
fo.delete_file("/home/user/Desktop/Automation/automationFiles/Braj.txt")



