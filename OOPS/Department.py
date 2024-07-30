#inheritance
class department:
    def dept_data(self):
        print("*******Department data******")
    def dept_name(self):
        print("Department name: MCA")
    def dept_num(self):
        print("Department number: 2001")
class employee1(department):
    def emp_data(self):
        print("*******Employee data******")
    def emp_name(self):
        print("Employee name: Alwin")
    def emp_age(self):
        print("Employee age: 22")
    def emp_gender(self):
        print("Employee gender: male")
    def emp_num(self):
        print("Employee number: 3214569875")

class employee2(department):
    def emp_name(self):
        print("Employee name: alwi")
    def emp_age(self):
        print("Employee age: 21")
    def emp_gender(self):
        print("Employee gender: female")
    def emp_num(self):
        print("Employee number: 2514639875")

obj = department()
obj.dept_data()
obj.dept_name()
obj.dept_num()
obj1 = employee1()
obj2 = employee2()
obj1.emp_data()
obj1.emp_name()
obj1.emp_age()
obj1.emp_gender()
obj1.emp_num()
obj2.emp_name()
obj2.emp_age()
obj2.emp_gender()
obj2.emp_num()