class employee:
    no_of_employees=0       #here it is called as a class variable
    company_name="Apple"    #here it is called as a class variable
    def __init__(self,name):
        self.name=name     #here it is called as a instance variable
        self.raise_amount=20000     #here it is called as a instance variable
        employee.no_of_employees +=1
    def show_details(self):
        print(f"The Employee {self.name} is working in {self.company_name} with {self.no_of_employees} and got a raised amount of {self.raise_amount}")
a=employee("Navneet")
a.show_details()
print(employee.company_name)
employee.company_name="google"
b=employee("saurabh")
b.show_details()
c=employee("Yash")
c.company_name="TCS"
c.show_details()
