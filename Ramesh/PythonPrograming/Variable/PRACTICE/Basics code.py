a = str(input("Enter the number :"))
b = str(input("Enter the number :"))
sum = (a+b)

print(sum)

print("___"*20)


a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

if a > b:
    print("The Largest number is :", a)
else:
    print("The Largest number is :", b)

print("___"*20)


a = int(input("Enter the value : "))

if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("___"*20)


a = int(input("Enter the number : "))

print("Square of the number is ", a**2)


print("___"*20)


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

a, b = b, a
print("The swap number of :", "a =", a)
print("The swap number of :", "b =", b)


print("___"*20)


# STRING PROGRAMS

str1 = input("Enter the string : ")

print("Reverse String is :", str1[::-1])


print("___"*20)


a = input("Enter the Character : ")
count = 0

for ch in a:
    if ch in "aeiou":
        count = count + 1
    else:
        continue

print("The vowels are : ", count)


print("___"*20)


a = input("Enter the character : ")

if a == a[::-1]:
    print("It is palindrome")
else:
    print("It's not Palindrome")


print("___"*20)


a = input("Enter the character : ")

print("It's upper case is : ", a.upper())
print("It's lower case is : ", a.lower())


print("___"*20)


a = input()
ch = input("Enter the character : ")

print("Count of the character is ", a.count(ch))


print("___"*20)

print("###"*20)

# if else problems 

a = int(input())

if a > 0:
    print("The number is Positive")
elif a < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


print("___"*20)


a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

if a >= b and a >= c:
    print("a is the greatest number", a)
elif b >= a and b >= c:
    print("b is the greatest number", b)
else:
    print("c is the greatest number", c)


print("___"*20)


age = int(input("Enter the age : "))

if age >= 18:
    print("He/She Eligible for the vote")
else:
    print("He/She Not Eligibe for the vote")


print("___"*20)


marks = int(input("Enter the marks = "))

if marks >= 90:
    print("Grade is : A")
elif marks >= 70:
    print("Grade is : B")
elif marks >=50:
    print("Grade is : C")
elif marks >= 40:
    print("Grade is : D")
else:
    print("FAIL")


print("___"*20)


print("###"*20)

# LOOPS PROGRAMES DONE 

for i in range(1, 11):
    print(i)


print("___"*20)


for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("___"*20)


a = int(input("Enter the number : "))
sum = 0

for i in range(1, a+1):
    sum = sum + i

print("Sum of the number is : ", sum)


print("___"*20)


a = int(input("Enter the number : "))

for i in range(1, 12):
    print(a, "x", i, "=", a * i)


print("___"*20)


a = int(input("Enter the number : "))
count = 0

while a > 0:
    a = a // 10
    count = count + 1
print("Digits are : ", count)


print("___"*20)