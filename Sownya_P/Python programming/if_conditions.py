a = 12

b = 11111

if a==b:
    print("a and b are equal")
else:
    print("a and b are not equal")  

print("-"*50)

### Even or ODD

# n1 = input("Enter a number: ")

 # if int(n1)%2==0:
 #    print("The number is even") 
 # else:
 #   print("The number is odd")  
 #
# ************** and & OR conditions *****************

#####      Greatest of 3 numbers
a = 220 
b= 220
c= 220

if a > b and a> c:
    print("a is the greatest number")       

elif b > a and b > c:
    print("b is the greatest number")
elif c > a and c > b:
    print("c is the greatest number")

else:
    print("none of them are equal")


##  *************  nested if condition ************

r1 = "pass"
r2 = "pass"
r3 = "fail"

if r1 == "pass":
    print(" You have passed Round 1")
    if r2 == "pass":
        print(" You have passed Round 2")
        if r3 == "pass":
            print(" You have passed Round 3 also ")
        else:
            print(" You have failed Round 3")
    else:
        print(" You have failed Round 2")
else:
    print(" You have failed all rounds")

print("*"*50)
###### nested else condition **********

rnd1 = "pass"

if rnd1 == "fail":
    print(" You have passed Round 1")
else:
    print(" You have failed Round 1")
    rnd2 = "fail"
    if rnd2 == "pass":
        print(" You has passed round 2" )
    else:
        print(" You have failed Round 2")
        rnd3 = "pass"
        if rnd3 == "pass":
            print(" You are qualified as Trainer")
        else:
            print(" You have failed Round 3")

print("-"*50)

