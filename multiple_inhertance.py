class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("The Name of Employee is : ",self.name)
        
class Programmer:
    def __init__(self,Lang):
        self.Lang=Lang
    def show(self):
        print("The Employee program's in ",self.Lang)
        
class employeee_as_programmer(employee,Programmer):
    def __init__(self,name,Lang):
        self.Lang=Lang
        self.name=name

a=employeee_as_programmer("Navneet Bhaltilak","Python and C++")
a.show()
print(employeee_as_programmer.mro())   #it gives the sequence of searching the methods in the class hierarchy