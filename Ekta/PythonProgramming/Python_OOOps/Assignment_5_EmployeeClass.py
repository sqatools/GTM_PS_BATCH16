class Employee:

    def __init__(self, name, age, salary):  #constructor method which is used to initialize the instance variables.
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee_details(self):  #instance method which is used to display the employee details.
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Salary:", self.salary)

obj=Employee("Vidya", 30, 50000)  #created object of the class and passed arguments to the constructor
obj.display_employee_details()  #called the instance method using the object of the class