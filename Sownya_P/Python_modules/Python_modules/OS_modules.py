import os

## basic usgae of OS Module in Python
print("$"*50)
# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

print("$"*50)
# List all files and directories in the current directory
files_and_dirs = os.listdir(current_directory)
print("Files and Directories in Current Directory:", files_and_dirs)

print("$"*50)

# List all files and directories in a specific directory one by one 

sowfiles = "C:\\AutomationProject\\GTM_PS_BATCH16"
items_in_directory = os.listdir(sowfiles)
print("Items in Directory:", items_in_directory)    
print("/"*50)

for item in items_in_directory:
    print(item)


print("-"*50)

import os

# Create a new directory
new_directory = r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python_programming\New_Directory"

if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created.")


## check file or directory exists
file_path = r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python_programming\New_Directory\example.txt"
file_path2 = r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python_programming\New_Directory"

print("folder exists :", os.path.exists(file_path2))
print("file exists : ", os.path.exists(file_path))


"""" in if loop to check 
if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")    

    """

# Change the current working directory to the new directory

os.chdir(new_directory)


# Get the current working directory after changing it
current_directory = os.getcwd()
print("Current Directory after changing:", current_directory)   

# Create a new file in the new directory
new_file = "example.txt"        
with open(new_file, 'w') as file:
    file.write("This is an example file created using the os module in Python.")
print(f"File '{new_file}' created in '{current_directory}'.")

# List all files and directories in the new directory
files_and_dirs = os.listdir(current_directory)
print("Files and Directories in New Directory:", files_and_dirs)    

# check whether file or directory exists

file_path3 = r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python_programming\Python_modules\OS_modules.py"
file_path4 = r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python_programming\Python_modules"
print("Is it a file? ", os.path.isfile(file_path3))
print("Is it a directory? ", os.path.isdir(file_path4))

print(" is it a file? ", os.path.isfile(file_path4))
print("is it a directory? ", os.path.isdir(file_path3))


# execute commands in the terminal using os module
os.system("notepad")  # will open notepad application
os.system("calc")   # will open calculator application
