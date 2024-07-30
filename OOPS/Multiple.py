class person:
    def person_info(self,name,age):
        print("Inside person class")
        print('Name:',name)
        print('Age:',age)

class company:
    def company_info(self,cname,location):
        print("Inside company class")
        print('Name:',cname)
        print('Location:',location)

class employee(company,person):
    def employee_info(self,emp_id,emp_name,emp_company):
        print("Inside employee class")
        print('Employee ID:',emp_id)
        print('Employee Name:',emp_name)
        print('Employee Company:',emp_company)


obj = employee()
obj.person_info('Alwin K G',22)
obj.company_info('Infosys','Mysore')
obj.employee_info(777,'KAG','Infosys')