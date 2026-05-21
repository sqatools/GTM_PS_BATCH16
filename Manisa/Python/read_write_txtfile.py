"""
date -4th april
r(read)-read content to file 
w(write)-write content to file(override)
a(append)-write content to file(doesnt override)
"""

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close

read_file(filepath=r"C:\PythonAutomation\GTM_PS_BATCH16\Manisa\Demo_File.txt")

def read_file_context_manager(filepath):
    #context manager has its own enter and exit method, it auto close the file when we move out of context manager
    with open(filepath, "r") as file:
         data = file.read()
         print(data)

read_file_context_manager(filepath=r"C:\PythonAutomation\GTM_PS_BATCH16\Manisa\Demo_File.txt")

#write content to file with write mode
#write content to non exitsing file

def write_content(filepath, content):
    #context manager has its own enter and exit method, it auto close the file when we move out of context manager
    with open(filepath, "w") as file:
         file.write(content)
         

"""text_file_path = "c:\PythonAutomation\GTM_PS_BATCH16\Manisa\write_content.txt"
file_content = "we are learning file handling"
write_content(filepath = text_file_path, content = file_content)"""

#write content to existing file

text_file_path = "c:\PythonAutomation\GTM_PS_BATCH16\Manisa\write_content2.txt"

file_content = "we are learning file handling, data is updated"
#write_content(filepath = text_file_path, content = file_content)

#append content to file
def append_content(filepath, content):
     
    with open(filepath, "a") as file:
         file.write(content)

file_name = "c:\PythonAutomation\GTM_PS_BATCH16\Manisa\write_context2.txt"
new_content = "adding content to the new file"
append_content(filepath=file_name, content=new_content)

    