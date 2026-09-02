class myclass:
    def __init__(self,value):
        self.value =value
    def show(self):
        print(f"The value is : {self.value}")
    @property
    def ten_value(self):
        return self.value*10
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value/10
a=myclass(10)

print(a.ten_value)
a.show()
