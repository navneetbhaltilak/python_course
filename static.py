class math:
    def __init__(self,num1):
        self.num1=num1
        print("__init__ function called : ",num1)
    def sum(self,num2):
        return print("sum method called : ",self.num1+num2)
    @staticmethod
    def add(a,b):
        return a+b
a=math(10)
a.sum(2)
print("Static method called :",math.add(2,4))