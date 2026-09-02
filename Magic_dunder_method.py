class employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):   #no need to call this method for object 
        return f"my Name is {self.name}".upper()
    
    def __repr__(self):  #used to recover an object and run when there is no str
        return f"my Name is {self.name}".lower()
    def __call__(self, *args, **kwds):
        pass
