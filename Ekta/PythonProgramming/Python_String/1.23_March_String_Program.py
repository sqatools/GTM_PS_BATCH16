str1="Hellow"
str2="Python"
str3=str1+str2
print(str3)
str3=str1+ " " +str2
print(str3)
number=100
# we can not concatenate string with number str3=str1+str2+number. we need to use conversion.
str3=str1+str2+str(number)
print(str3)

# F string formating also we used instaed of concatenation
name="Ekta"
age=35
city="Pune"
result=f"My name is {name}.My age is {age}.I am from {city}city"
print(result)

#String slicing str[start:end:step value]
str="Pythong Programming"
print("String slicing result1--->",str[0:6:1])
#default start value is 0. default end value is end of string . default step value is 1.
print("String slicing result2--->",str[7::])
print("String slicing result3--->",str[::2])
print("String slicing result4--->",str[::])

#if step value is -ve then default start value -1,end value is start of string . to reverse string we can use this
print("String slicing result --->",str[::-1])

###STring Methods###
#1.Upper and Lower method
str="I am learning python yuppyyy!!!"
print("Convert stattement into lower case",str.upper())
print("Convert statement into upper case",str.lower())
#2.title() - it print first letter of each statment in capital
print("First letter of each statement in capital",str.title())
#3.swapcase() - conevert uppercase to lowercase and lower case to upper case
print("convert upper to lower and lower to upper",str.swapcase()) #i AM LEARNING PYTHONG YUPPYYY!!!
#4. count()- we can get how many times caracter or word is get repeated 
str="Python is good langauge. Learning python is easy. You need daily study for python"
print("Calculate o in above statement ",str.count("o"))
print("Calculate Python word in above statement",str.count("Python")) # Its case sensitive
#5.index --> this method return index of character or word 
print("index of n in above string --> ",str.index("n"))
#6. split()--split any given string with delimetres and return o/p in list format. sepearted by ,   
str1="Python is very easy to learn"
str2="India-is-best-cricket-team"
str3="Automation,with,AI"
print("Split with space-->",str1.split(" "))
print("Split with - --->",str2.split("-"))
print("split with , --->",str3.split(","))
print("split with p --->", str1.split("P"))
str4="PythongProgrammingPLangauge"
print("Split with p --->",str4.split("P"))
#7.replace()-- this method is used to replace any given word with other word"
str="Java is programming langague.Java is easy to learn.Java is secure langague"
print("Replace java with python --->", str.replace("Java","Python"))
print("Replace 2 java with python --->", str.replace("Java","Python",2)) # first two java keywords get replace with python
#8.Strip() -- removes trailing spaces from given string (Ask on this )
print("*"*50)
str="    Pyhton Program "
print("Before using strip method-->",str)
print("Remove extra spaces -->",str.strip())
print(str.strip())
print("*"*50)
str1= "    Pythong Program "
print("Before using split function", str1)
print("After using split function",str1.strip())
#Join method---> To join list of string we use join method

list1=["Hellow", "I","am","Ekta"]
result="-".join(list1)

print("Joining list -->",result)
result=" ".join(list1)
print("joining with spaces only--->",result)

string_c="India"
print("*".join(string_c))

# Program to remove duplicates words from string

strwords="Rahul Ravi Rohan Rohit Rahul Ravi Ronak Roshan"
output=strwords.split()
result=[]
for word in output:
    if word not in result:
        result.append(word)

        final=''.join(result)
        
        print(final)

text=",,,,%%cgc... ekta...***  "
print("Strip method:",text.strip("%*"))
print("Strip method:",text.strip(" ,.%gc*"))

b = "Hello, World!"
print(b[-5:-2])




