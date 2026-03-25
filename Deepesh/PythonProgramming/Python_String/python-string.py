str1 = "Hello"
str2 = "Python"
num = 123

# string cancatenation
str3 = str1 + " " + str2 + " "+str(num)
print("str3 :", str3) # str3 : Hello Python 123

# F string formating.
name = "Rahul"
age = 25
city = "Mumbai"
result = f"Hello my name is {name}, age is {age} and live in {city}"
print("result :", result)
# Hello my name is Rahul, age is 25 and live in Mumbai

#########################################
# string slicing :  str[start: end: step]
str2 = "Python Programming"
print(str2[0:6:1])  # Python

# default end value is end of string, default step value is 1
print(str2[7::]) # Programming

# default start value is zero, end value is end of string
#  if step value is +ve
print(str2[::2]) # Pto rgamn
print(str2[::]) # Python Programming


# default start value will be -1, and end value is start of string, 
# if step value is -1
print(str2[::-1]) # gnimmargorP nohtyP

###################### String Methods #################
# Upper() and Lower()
str_a = "hello wE Learing PyThoN"
print("Upper Result :", str_a.upper())
# HELLO WE LEARING PYTHON
print("Lower Result :", str_a.lower())
# hello we learing python

# title(): First letter of each word in capital case.
print("title :", str_a.title()) # Hello We Learing Python

# swapcase : convert upper to lower and lower to upper
print("swapcase :", str_a.swapcase())
# HELLO We lEARING pYtHOn

print("_"*50)
######################################
str_b = "Python is very to learn"

# count method : get count of char/word from string.
print("count of e:", str_b.count('e')) # count of e: 2
print("count of is :", str_b.count("is")) # count of is : 1

# index method : this method return index position of any char/word.
print("Index of i :", str_b.index("i")) # Index of i : 7


######################################
str_c = "Python is very to learn"
str_d = "India-is-best-cricket-team"
str_e = "Automation#with#AI"
str_f = "ytPhonmProgrammingPLearning"
url = "https://facebook.com"

# split method: this method split any given string with delimeters and return output.
print("split with space :", str_c.split(" ")) # ['Python', 'is', 'very', 'to', 'learn']
print("split with - :", str_d.split("-")) # ['India', 'is', 'best', 'cricket', 'team']
print("split with # :", str_e.split("#")) # ['Automation', 'with', 'AI']
print("split with P :", str_f.split("P")) # ['yt', 'honm', 'rogramming', 'Learning']
print("domain :", url.split("//")[1].split(".")[0]) # facebook

##############################
# replace method :this method replace any given word with another word.

str_11 = "JAVA Programming is Easy to Learn, JAVA is Secure, JAVA support OOPS"
result = str_11.replace("JAVA", "Python")
print("Replace all result :", result)
# Python Programming is Easy to Learn, Python is Secure, Python support OOPS

result2 = str_11.replace("JAVA", "Python", 2)
print("Replace first 2 JAVA count result :", result2)
# Python Programming is Easy to Learn, Python is Secure, JAVA support OOPS

print("_"*50)
#############################################
# strip method : method to remove trailing spaces from given string.
# means it will remove all the spaces in the begining and end of string.
str_12 = "  Python Programming  "
print(str_12)
print(str_12.strip())

print("_"*50)
#############################################
# join method : If we want to join any particulat list of string. to generate new string.
list1 = ["Hello", "Good", "Morning"]

result = "-".join(list1)
print("result :", result) # Hello-Good-Morning

print(" ".join(list1)) # Hello Good Morning

str_m = "Cricket"
print("$".join(str_m)) # C$r$i$c$k$e$t

print("".join(str_m)) # Cricket

print("_"*40)
######################################
# isnumeric :  this method if string contains only numbers.

s1 = "465464"
s2 = "8976897 443"
print(s1.isnumeric()) # True
print(s2.isnumeric()) # False


# isalpha() : this method check string only contains alphabastes.

s3 = "Hello"
s4 = "Python Program"
print(s3.isalpha()) # True
print(s4.isalpha()) # False

# isalnum() : This method check string contains alphbates and numbers.

s5 = "Learning Python"
s6 = "Program12345"
print(s5.isalnum()) # False
print(s6.isalnum()) # True

