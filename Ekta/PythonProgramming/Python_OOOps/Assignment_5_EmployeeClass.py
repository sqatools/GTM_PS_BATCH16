class Employee:

    def __init__(self, name, age, salary):
        print("Constructor called automatically when object is created")  
        self.Ename = name
        self.Eage = age
        self.Esalary = salary

    def display_employee_details(self):  #instance method which is used to display the employee details.
        print("Employee Name:", self.Ename)
        print("Employee Age:", self.Eage)
        print("Employee Salary:", self.Esalary)

obj=Employee("Vidya", 30, 50000)  #created object of the class and passed arguments to the constructor
obj.display_employee_details()  #called the instance method using the object of the class

obj1=Employee("Rakesh", 28, 60000)  #created another object of the class and passed arguments to the constructor
obj1.display_employee_details()  #called the instance method using the object of the class

