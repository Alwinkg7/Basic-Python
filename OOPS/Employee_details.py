class Employee:
    def __init__(self, name,age,salary,phone):
        self.name = name
        self.age = age
        self.salary = salary
        self.phone = phone
    def displayDetails(self):
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        print("Employee Phone: ",self.phone)

obj1 = Employee("David",23,50000,1200556546)
obj2 = Employee("Davi",24,40000,2000345631)
obj1.displayDetails()
obj2.displayDetails()