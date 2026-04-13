"""
r(read) : read mode the file content
w(write) : write content to the file (override previous content)
a(append) : write content to file (doesn't override the previous content)

"""

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

text_file_path = r"C:\GitCode\GTM_PS_BATCH16\Ramesh\PythonPrograming\Variable\Handles_File\read_data.txt"
# read_file(filepath=text_file_path)


def read_file_context_manager(filepath):
    # context manager has its own enter and exit method, it auto close the file when we move out of
    # context manager.
    with open(filepath, "r") as file:
        data = file.read()
        print(data)

# read_file_context_manager(filepath=text_file_path)


# write content to file with write mode.


def write_content(filepath, content):
    with open(filepath, "w") as file:
        file.write(content)

"""
#1. write content to non-existing file: It will creat file and add content
text_file_path = "write_content.txt"
file_content = "We are learning file handaling"
write_content(filepath=text_file_path, content=file_content)


# 2. write content to existing file : It will override the existing file and add content to the file

text_file_path = "write_content2.txt"
file_content = "We are learning file handaling here data is updated with write mode"
write_content(filepath=text_file_path, content=file_content)
"""



####################################################################

# append content to the file


def append_content(filepath, content):
    with open(filepath, "a") as file:
        file.write(content)
"""
#1. append content to non-existing file: It will creat file and add content.

file_name = "append_data.text"
new_content = "Adding content to new file and data should be visible"
append_content(filepath=file_name, content=new_content)
"""

#1. append content to non-existing file: It will creat file and add content.

file_name2 = "append_data2.text"
new_content = "\nAdding content to new file at end of the file"
append_content(filepath=file_name2, content=new_content)