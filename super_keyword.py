class employee:
    def __init__(self,Id,name):
        self.Id=Id
        self.name=name
    def show(self):
        print(f"Name of an employee we Id {self.Id} is Mr.{self.name}")

class Programmer(employee):
    def __init__(self,Id,name,lang):
        super().__init__(name,Id)  #here we use the super class 
        self.lang=lang
        print(f"Name of a Programmer we Id {self.Id} is Mr.{self.name} working on {self.lang}")
navneet=employee("Navneet Bhaltilak",13092005)
navneet.show()
Saurabh=Programmer("Navneet Bhaltilak",13092005,"python and c++")