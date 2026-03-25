# 1. write a python program to remove duplicate characters
# from given string.

str1 = "Learning Python is Fun"
output = ""

for char in str1:
    print(output)
    if char not in output:
        output = output + char
    else:
        continue

print("Output :", output) # Learnig PythosFu


#Q2 write python program to remove duplicate words.
str2 = "Rahul Ravi Rohan Rohit Rahul Ravi Ronak Rohan"


#Q3 write python program to longest words from given string.
str3 = "India won third t20 cricket world cup"

str4 = "Python"
print(len(str4))
w1 = str4[:2]
w2 = str4[-2:]
print(w1+w2)