class alternate:
    def __init__(self,name,salary):
        self.name=name.upper()
        self.salary=salary
    @classmethod
    def alt_string(self,string):
        return self(string.split("-")[0],int(string.split("-")[1]))
    def show(self):
        print(f"{self.name} has {self.salary} as a monthly salary")
a=alternate("navneet",200000)
a.show()

b=alternate.alt_string("Saurabh-300000")
b.show() 