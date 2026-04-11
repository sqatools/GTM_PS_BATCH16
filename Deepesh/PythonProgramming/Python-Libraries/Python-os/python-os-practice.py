import os
import time

# Get the current working directory#
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# Current Directory: E:\Trainings\GTM_PS_BATCH16_Mar2026\GTM_PS_BATCH16\Deepesh\PythonProgramming\Python-Libraries

#join 2 path
tar_path = r"E:\Filesdata\Batch15"
file_name = "count_name.txt"
file_path = os.path.join(tar_path, file_name)
print("filepath :", file_path) 
# E:\Filesdata\Batch15\count_name.txt

# check target path is exist or not.
tar_path2 = r"E:\Filesdata\Batch15\testdata.txt"
tar_path3 = r"E:\Filesdata\Batch15\count_name.txt"
print("Path 2 exist :", os.path.exists(tar_path2)) # False
print("Path 3 exist :", os.path.exists(tar_path3)) # True

# check given path is a folder or file.
tar_path5 = r"E:\Filesdata\Batch15"
tar_path6 = r"E:\Filesdata\Batch15\count_name.txt"

print("check path5 is folder:", os.path.isdir(tar_path5))
# check path5 is folder: True
print("check path6 is file:", os.path.isfile(tar_path6))
# check path6 is file: True
print("check path5 is file:", os.path.isfile(tar_path5))
# check path5 is file: False


# create directory.
tar_path7 = r"E:\Filesdata\Batch16"
if not os.path.exists(tar_path7):
    os.mkdir(tar_path7)


time.sleep(2)
# remove folder
if os.path.exists(tar_path7):
    os.rmdir(tar_path7)


# run windows command
os.system("mkdir E:\\filesdata\\batch16")
os.system("dir E:\\")






