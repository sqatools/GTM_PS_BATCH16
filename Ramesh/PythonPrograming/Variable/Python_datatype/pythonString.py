str1 = "Hello"
str2 = "Pyhon"
num = 123

# String Concatenation 
str3 = str1 + " " + str2 + " " + str(num)

print(str3)

# F string formating 

name = "Ramesh"
age = 28
city = "Guwahati"

result = f"Hello my name {name}, my age {age}, and i live in {city}"
print (result)

######################################
# String slicing : str[start: end; step]

str2 = "Python Programming"
print(str2[0:6])

print(str2[7::])
print(str2[::2])

# default start value will be -1 , and value is start of string 
# if step value is -1

str3 = "Hello Ramesh"
print(str3[::-1])

########### STRING METHOD ############################
# 1. upperCase and lowerCase

str_a = "hello we are learning python"
str_b = "HELLO WE ARE LEARNING PYTHON"
print(str_a.upper())
print(str_b.lower())

# title(): First letter of each word in capital case.
print(str_a.title())
print(str_a.swapcase())

#################################################

str_c = "Python is very easy to learn"
print(str_c.count("a"))

# index method : this method return index position of any char/word

print(str_c.index("is"))


####################################################

str_d = "Python is very easy to learn"
str_e = "India-is-best-cricket-team"
str_f = "Automation#with#AI"
str_g = "ytohonmProgrammingPLearning"
url = "https://facebook.com"

# split method : this method split any given string with delimeters and return output.

print(str_d.split(" "))
print(str_e.split("-"))
print(str_f.split("#"))
print("split with P :", str_g.split("P"))
print("domain :", url.split("//")[1].split(".")[0]) # facebook


############################################################################

# replace method : this methode replace any word with another word

str_11 = "JAVA Programing is easy to learn, JAVA is secure, JAVA supports OOPS"
result = str_11.replace("JAVA", "Python", 2)
print("Replace 2 result : ", result)


#####################################################

# strip method : metod to remove trailing spaces from given string 

str_12 = "  Python Programmin  "
print(str_12)
print(str_12.strip())


#########################################################################
# join method : if we want to join any particular list of string . to generate new string 

list1 = ["Hello" , "good" , "Morning"]

result = "-".join(list1)
print(result)
print(" ".join(list1))

str_i = "Cricket"
print(" ".join(str_i))


##############################################


# isnumeruc : this method if string contains only numbers.

s1 = "2323423"
s2 = "5236463 634"

print(s1.isnumeric())
print(s2.isnumeric())

# isalpha() : this method check string only contains alphabates.

s3 = "Hello"
s4 = "Python Program"

print(s3.isalpha())
print(s4.isalpha())


# isalnum() : this method check string contains alphabates and numbers.

s5 = "Learning Python"
s6 = "Program12345"

print(s5.isalnum())
print(s6.isalnum())