str1 = " hello"
str2 = " Python"

num= 1234

## string concatination ###

str3 = str1 + " " + str2
print(str3)

str3 = str1 + "" + str2 + "" + str(num)
print(str3)


## F string Formating 

name = "sownya"
age = 30 

place = "hyd"

result = f"hello my name is {name} and my age is {age} and i am from {place}"

print(result)

print("*"*50)

### string slicing ## 
### Format for string slicing is [start:end:step]

str12 = "python programming"

print(str12[2::])

print(str12[0:6:1])

print(str12[::2])

print(str12[:6:])

print("-"*50)

print(str12[-1:-17:-1])


### string Methods ###

### 1. Uppercase and Lower Case --- Upper() and Lower()

str1= "we are learning Python"

print(str1.upper())
print(str1.lower())

## 2. first letter of each word in capital  -- title()


print("*"*50)

str1= "wE aRe learNing PytHon" 

print(str1.title())

#swap case from upper to lower and lower to upper

print(str1.swapcase())

print("*"*50)

### 

strg2= "python is very easy to learn"

## get count of particular letter

print(strg2.count("e"))

print(strg2.count("you"))

## method to return index position of any character or word 

print(strg2.index("i"))


str_a= "python is a programming language"   
str_b = "which-has-better-future"
str_c = "for#automation#using@AI "

print("split with space : ", str_a.split())

print("split with - ", str_b.split("-"))

print("split with #",  str_c.split("#"))


domain =" https://facebook.com"

print(domain.split("//"))

print(domain.split("//")[1])

print(domain.split("//")[1].split(".")[0])


## replace method to replace any word or character with another word or character

str1 = " Java is easy to learn,Java is used for automation and java uses oops concept"

print(str1.replace("Java","Python"))

# replacing Java 2 times with python 

print(str1.replace("Java","Python", 2))

## strip method removes spaces from the beginning and end of the string

str2 = "   hello world   "  

print(str2.strip())

print("-"*50)

## Join method to join the list of string with any character 

list1 = ["python", "is", "a", "programming", "language"]    

res= "-".join(list1)
print(res)

str11 ="SownyaSreePothukuchi"

print(" ".join(str11))

## qstn === how can we procide space between words using join method ?
#  ##is it through list ? 