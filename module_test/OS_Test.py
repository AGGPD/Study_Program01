import os


'''
if os.path.exists("user/mofan"):
    print("Yes, it exists")
else:
    os.makedirs("user/mofan")
    print("No, it doesn't exist, but I just created it")
print(os.listdir("user"))

os.remove("user/mofan_new") # remove the file
# import shutil
# shutil.rmtree("user/mofan") # remove the folder and all its content

os.makedirs("user/mofan",exist_ok=True) # exist_ok=True, if the folder exists, it won't raise an error
with open("user/mofan/a.txt", 'w') as f:
    f.write("nothing")
print(os.path.isfile("user/mofan/a.txt")) # True
print(os.path.exists("user/mofan/a.txt")) # True
print(os.path.isdir("user/mofan/a.txt")) # False
print(os.path.isdir("user/mofan"))  # True
print(os.path.getsize("user/mofan_new")) # 7
'''

import shutil

def copy(path):
    file_name = os.path.basename(path)
    dir_name = os.path.dirname(path)
    new_file_name = file_name + "_copy"
    new_path = os.path.join(dir_name, new_file_name)
    shutil.copy(path, new_path)
    return os.path.isfile(new_path), new_path
copied,new_path = copy("user/mofan/a.txt")
if copied:
    print("Copied successfully to", new_path)
else:
    print("Failed to copy")

