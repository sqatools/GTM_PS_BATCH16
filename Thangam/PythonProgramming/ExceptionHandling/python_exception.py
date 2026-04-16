def calculate():
    try:
        n1 = 10
        n2 = "Python"
        n3 = n1 + n2
    except Exception as e:
        print(f"Exception error :{e}")
        print("Can not add number with string")

calculate()
print("Calculation is completed")

