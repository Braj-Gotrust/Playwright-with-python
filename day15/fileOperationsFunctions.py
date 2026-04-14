import os
import shutil

# 1. Write a file (create a new if not exist, override if exist)
def write_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"File successfully written {file_path}")


# 2. Append data into exist file
def append_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)
    print(f"File successfully append {file_path}")


# 3. Read text file
def read_to_file(file_path, mode='all'):
    with open(file_path, "r") as file:
        if mode == 'all':
            return file.read()
        elif mode == 'line':
            return file.readline()
        elif mode == 'lines':
            return file.readlines()
        else:
            raise ValueError("Invalid file mode. This is use 'all' or 'line' or 'lines'")



# 4. Rename file
def rename_file(source, target):
    os.rename(source, target)
    print(f"File successfully renamed from {source} to {target}")

# 5. Deleting a file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File successfully deleted from {file_path}")
    else:
        print(f"File {file_path} does not exist")


# 6. create a directory
def create_directory(dir_path):
    os.mkdir(dir_path)
    print(f"Directory {dir_path} created successfully")



# 7. checking if a directory exist
def check_dir_exists(dir_path):
    return os.path.exists(dir_path)


# 8. Rename directory
def rename_directory(source, target):
    os.rename(source, target)
    print(f"Directory {source} renamed to {target}")


# 9. remove directory
def remove_directory(dir_path, force=False):
    if force:
        shutil.rmtree(dir_path)  # Remove if not empty
    else:
        os.rmdir(dir_path)   # only remove if empty
    print(f"Directory {dir_path} removed successfully")


# 10. get current working directory
def get_current_directory():
    return os.getcwd()


