def read_file(file_path):
    file = open(file_path, 'r')
    content = file.read()

    print("file content:", content)
    
    file.close()    

 ## read_file('read_data.txt') -- if i want to read the file from current directory 
text_file_path = r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\read_data.txt"

read_file(file_path=text_file_path)

read_file(file_path= r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Demo File.txt.txt")
##-- if i want to read the file from specific directory


## write content to a file  

def write_file(file_path, content):
    file = open(file_path, 'w')
    file.write(content)
    file.close()    

write_file(file_path=r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\write_data.txt", content="This is the content to be written to the file.")
## this will be completely overwrite the existing content in the file. 
# If the file does not exist, it will be created.

write_file(file_path=r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\abc_text.txt", content="This is the new content to be written to the file.")

## append content to a file 

def append_file(file_path, content):
    file = open(file_path, 'a')
    file.write(content)
    file.close()

append_file(file_path=r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\write_data.txt", content="\nThis is the additional content to be appended to the file.")  

append_file(file_path=r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\xyz_text.txt", content="\nThis is the additional content to be appended to the file.")


## context manager to handle file operations

def read_file_with_context_manager(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content) 
        print("is file closed?", file.closed)  # Check if the file is closed after the block  

    print("is file closed after the context manager block?", file.closed) 
    # Check if the file is closed after the block    
      
read_file_with_context_manager(file_path='abc_text.txt')
