#function call without storing value in variable 
def getsquare(n):
    return n**2
print("square of number", getsquare(100))

#function call with storing value in variable
def gettripple(n):
    return n**3
result=gettripple(5)
print("Tripple of 5", result)
 # return statement break the function execution immediately
def get_sum_values(n):
    sum=0
    for i in range(1,n+1):
        print(i)
        if i==5:
         return sum
        sum=sum+i #this code is unreachable as we written this after return keyword
sum_result=get_sum_values(10)
print("Sum of values",sum_result)
    