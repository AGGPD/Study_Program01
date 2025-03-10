import os
import re
'''

string = "这是我的主页 https://mofanpy.com, 这个 www.mofanpy.com 有很多 mofan 教你机器学习和 python 语言的教学"
res = re.findall(r"(https://)?(mofanpy.com)", string)
for r in res:
    print(r)

'''
# define directory
directory = "files"

# iterate over each file in that directory
for filename in os.listdir(directory):
    # construct full file path
    file_path = os.path.join(directory, filename)

    #open and read the file content
    with open(file_path, "r") as f:
        content = f.read()
    
    #replace the target string
    update_content = re.sub(r"morvanzhou.github.io.com", "mofanpy.cn", content)

    #define new file path
    new_file_path = os.path.join(directory, "new_"+filename)

    # write the updated content to a new file
    with open(new_file_path, "w") as new_f:
        new_f.write(update_content)


# Now, iterate over the directory to access each new file and print its content
print("\nAccessing each new file:")
for filename in os.listdir(directory):
    if filename.startswith("new_"):  # Check if the file is one of the new files
        new_file_path = os.path.join(directory, filename)
        with open(new_file_path, "r") as f:
            print(f"\nContent of {filename}:")
            print(f.read())

# delete the new files
for filename in os.listdir(directory):
    # Check if the filename starts with "new"
    if filename.startswith("new"):
        file_path = os.path.join(directory, filename)
        # Confirm it's a file before attempting deletion
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")