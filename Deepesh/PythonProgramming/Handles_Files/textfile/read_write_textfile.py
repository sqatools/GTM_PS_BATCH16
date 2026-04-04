"""
r(read) :  read mode to read the file content
w(write) : write content to file (override previous content)
a(append) : write cotent to file (doesn't override the previous content)
"""

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

text_file_path = r"E:\Trainings\GTM_PS_BATCH16_Mar2026\GTM_PS_BATCH16\Deepesh\PythonProgramming\Handles_Files\read_data.txt"
#read_file(filepath=text_file_path)

def read_file_context_manager(filepath):
    # context manager has its own enter and exit method, it auto close the file when we move out of 
    # context manager.
    with open(filepath, "r") as file:
        data = file.read()
        print(data)


#read_file_context_manager(filepath=text_file_path)

# write content to file with write mode.

def write_content(filepath, content):
    with open(filepath, "w") as file:
        file.write(content)


#1. write content to non-existing file :  It will create file and add content.
"""
text_file_path = "write_content.txt"
file_content = "we are learning file handling"
write_content(filepath=text_file_path, content=file_content)
"""


#2. write content to existing file :  It will override the existing file and add content to the file.
"""
text_file_path = "write_content2.txt"
file_content = "we are learning file handling, here data is updated with write mode"
write_content(filepath=text_file_path, content=file_content)
"""

#####################################################
# append content to the file


def append_content(filepath, content):
    with open(filepath, "a") as file:
        file.write(content)


#1. append content to non-existing file :  It will create file and add content.
"""
file_name = "append_data.txt"
new_content = "Adding content to new file and data should be visible"
append_content(filepath=file_name, content=new_content)
"""

#1. append content to non-existing file :  It will create file and add content.
file_name2 = "append_data2.txt"
new_content = "\nAdding content to new file at end of the file"
append_content(filepath=file_name2, content=new_content)