# Directory means like a folder
# Create a directory or folder

# # Create a directory
# import os
# os.mkdir("/home/user/Desktop/Automation/automationFiles/myDirectory1")
# print("Directory created successfully")

# After create the directory to check or not
import os
dir_path = "/home/user/Desktop/Automation/automationFiles/myDirectory1"
if os.path.exists(dir_path):
    print("Directory exists")
else:
    print("Directory does not exist")

# # Rename the directory
# import os
# os.rename("/home/user/Desktop/Automation/automationFiles/myDirectory1","/home/user/Desktop/Automation/automationFiles/myDirectory")
# print("Directory renamed successfully")

# # rmdir() -> Remove/Delete directory
# import os
# import shutil
# #os.rmdir("/home/user/Desktop/Automation/automationFiles/myDirectory1") # if directory is empty no some file contain then remove this method otherwise use another method
# shutil.rmtree("/home/user/Desktop/Automation/automationFiles/myDirectory1") # if directory contain some files then it will use
#
# print("Directory has been removed")


# getcwd() -> get the current working directory
import os
dir_path=os.getcwd()  # return current working directory
if os.path.exists(dir_path):
    print("Directory exists")
    print(dir_path)
else:
    print("Directory does not exist")
