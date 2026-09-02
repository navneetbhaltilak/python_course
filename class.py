class person:
    name="Navneet"
    occupation="Software Developer"
    net_worth=1000000
    def info(self):
        print(f"{self.name} is a {self.occupation} with a networt of {self.net_worth}")
a=person()
a.info()
b=person()
b.name="Saurabh"
b.occupation="Gambler"
b.net_worth=6000000
b.info()