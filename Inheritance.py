class employee:
    def __init__(self,name,id):
        self.name =name
        self.id=id
    def show(self):
        print(f"Mr.{self.name} has Employee_id {self.id}")
e1=employee("Navneet",3452)
e1.show()
class programmer(employee):   #this is a syntax to inherit any of the class
    def lan(self):
        print("It is an inherited class from the class employee")
e2=programmer("Saurabh",7652)
e2.lan()
e2.show()

