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

