class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by the animal")
class cat(animal):
    def __init__(self, name, bread):
        super().__init__(name,species ="cat")
        self.bread=bread
    def make_sound(self):
        print("Meow meow.......")
c=cat("Tom","Persiaan")
c.make_sound()
a=animal("Cat","cat")
a.make_sound()