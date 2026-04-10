print("My first prime number program")
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if n % i == 0:
        is_prime = False
        break
    print("is_prime")
    else