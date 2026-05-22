#date = 7th april

n1 = 40
n2 = "python"

#addition = n1 + n2
#print("addition:", addition) #error
#print("calculation is completed")

##############################################

def calculate(n1, n2):
      
      try:
            #n1 = 2
            #n2 = "python" #for error testing purpose
            addition =n1+n2
            print("addition is :", addition)
      except Exception as e:
            print("exception error :", e) #system error
            print("cannot add number with string")

calculate(10, "python")
print("calculation is with error completed")

calculate(10, 20)
print("calculation is succesfully completed")

#try except and else block
def calculate(n1, n2):
      
      try:
            addition =n1+n2
      except Exception as e:
            print("exception error :", e) #system error
            print("cannot add number with string")
      else:
            print("addition is :", addition)
            print("calculation is succesfully completed") #else block is executed when there is no error in try block

calculate(10, 100)

#try except else and finally block
def calculate(n1, n2):
      
      try:
            addition =n1+n2
      except Exception as e:
            print("exception error :", e) #system error
            print("cannot add number with string")
      else:
            print("addition is :", addition)
            print("calculation is succesfully completed") #else block is executed when there is no error in try block
      finally:
            print("calculation is completed with or without error") #finally block is executed always

calculate(10, 100)
print("with error part")
calculate(10, "python")

#handle multiple exceptions
print("----------------------------------------------------------------")
def calculate(n1, n2, n3):
      
      try:
            addition =n1+n2+n3
      except TypeError as e:
            
            #raise e #raise keyword is used to raise the exception again after handling it
            print("type error :", e) #system error
      
      except Exception as e:
            print("exception error :", e) #system error
            print("some other error occurred")
      else:
            print("addition is :", addition)
            print("calculation is succesfully completed") #else block is executed when there is no error in try block
      finally:
            print("calculation is completed with or without error") #finally block is executed always

print("with error part")
calculate(10, 20, "python")
calculate(10, 20, 30)
