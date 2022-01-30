class Company:

    def __init__(self, name, project):
        self.name_of_company = name
        self._project_name = project

    def print_details(self):
        print(f"Name of the company = {self.name_of_company}")
        print(f"Name of project = {self._project_name}")


class Employee(Company):
    def __init__(self, eName, salary, company_name, project_name):
        Company.__init__(self, company_name, project_name)
        self.employee_name = eName
        self.employee_salary = salary

    def print_salary_details(self):
        print(f"Salary of {self.employee_name} is {self.employee_salary}")


company = Company('Sigmoid', 'ABC Bank')
print(company.name_of_company)
print(company._project_name)

employee_1 = Employee("John", 2000, company.name_of_company, company._project_name)
print(f"Hello {employee_1.employee_name}, welcome to {employee_1.name_of_company}. You will be working in {employee_1._project_name} and your salary is {employee_1.employee_salary}")
