import os
import time


# get the current working directory
current_directory = os.getcwd()
print("current Directory:" , current_directory)
# current Directory: C:\GitCode\GTM_PS_BATCH16

print("----"*20)
# join 2 path
tar_path = r"C:\GitCode\GTM_PS_BATCH16\Ramesh\PythonPrograming\Variable\__pycache__"
file_name = "Function_file1.cpython-313"
file_path = os.path.join(tar_path,  file_name)
print(file_path)
# C:\GitCode\GTM_PS_BATCH16\Ramesh\PythonPrograming\Variable\__pycache__\Function_file1.cpython-313


print("--"*20)
# check target path is exist or not.
tar_path2 = r"C:\GitCode\GTM_PS_BATCH16\Ramesh\PythonPrograming\Variable\__pycache__\testdata.txt"
tar_path3 = r"C:\GitCode\GTM_PS_BATCH16"
print("path 2 exist:", os.path.exists(tar_path2))
print("path 3 exist:", os.path.exists(tar_path3))


# check given path is a folder or file 

tar_path4 = "C:\GitCode\GTM_PS_BATCH16"
tar_path5 = "Function_file1.cpython-313"
print(os.path.isdir(tar_path4))
print(os.path.isfile(tar_path5))

print("--"*20)

# create directory
tar_path6 = r"C:\GitCode\GTM_PS_BATCH16"
if not os.path.exists(tar_path6):
    os.mkdir(tar_path6)


# time.sleep(2)
# # remove folder

# if os.path.exists(tar_path6):
#     os.rmdir(tar_path6)


# run windows command
os.system("mkdir C:\\GitCode\\batch16")
os.system("dir C:\\")



