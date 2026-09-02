class employee:
    company_name="Google"
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"{self.name} is working in {self.company_name}")
    @classmethod   #operates an te class variable changes remain permanent
    def change_company(self,c_name): #here the self is a class that why it changes the class variable
        self.company_name=c_name
a=employee("Navneet")
a.show()
print(employee.company_name)
b=employee("Saurabh")
b.change_company("Tesla")
b.show()
print(employee.company_name)
c=employee("Yash")
c.change_company("Microsoft")
c.show()
print(employee.company_name)
