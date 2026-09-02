class person:
    def __init__(self,n,o,w):   #calling the function constructor
        self.name = n
        self.occupation=o
        self.net_worth=w
    def info(self):
        print(f"{self.name} is a {self.occupation} with a networt of {self.net_worth}")
# a=person()
# a.info(
# a.info()
a=person("Navneet","Software Developer",1000000)
b=person("Saurabh","Gambler",1000000)
a.info()
b.info() 