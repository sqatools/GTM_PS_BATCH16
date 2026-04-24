class Employee:
    company_name = "ABC Corporation"

    def __init__(self, name, age, salary):
        self.name = name
        self.emp_age = age
        self.emp_salary = salary

    def Emp_name(self):
        print("Name: ", self.name)

    def age(self):
        print("Age: ", self.emp_age)

    def salary(self):
        print("Salary: ", self.emp_salary)

    def display_Emp_details(self):
        self.Emp_name()
        self.age() 
        self.salary() 


emp1 = Employee("Aniket", "25", "50000")  
emp1.Emp_name()
print(emp1.company_name)
emp1.display_Emp_details()
print("--------------------------------------------------")
emp2 = Employee("Rahul", "30", "60000")
emp2.Emp_name()     
print(emp2.company_name)
emp2.display_Emp_details()


#hello world