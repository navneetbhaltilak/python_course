class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j-{self.k}k"
    def __add__(self,x):
        # return (f"{self.i+x.i}i+{self.j+x.j}j-{self.k+x.k}k")   it give a string data
        return vector(self.i+x.i,self.j+x.j,self.k+x.k)
a=vector(2,4,3)
print(a)
b=vector(1,1,1)
print(b)
print(a+b)
print(type(a+b))