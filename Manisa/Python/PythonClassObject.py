class employee:

    #constructor method which is used to initialize the instance variables.
    def __init__(self, name, age, salary):  
        print("please check the employee details:")
        self.name = name
        self.age = age
        self.salary = salary

    '''def display_employee_details(self):  #instance method which is used to display the employee details.
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Salary:", self.salary)

    #instance method
    def showEmpName(self):
        print("Employee Reporting is ", self.name)

    def EmpDetails(self):
        print("Employee Name:", self.name)
        print("Employee age:", self.age)
        print("Employee salary:", self.salary)'''


#create object of the class
obj = employee("Hari", "32" , "12000000")
obj.showEmpName()
obj.EmpDetails()



class Car:
    def __init__(kelf):
        print("constructor called")

    print("1233")

car1 = Car()


