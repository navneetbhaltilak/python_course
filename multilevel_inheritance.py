class animal:
    def __init__(self, name, species):
        self.name = name
        self.species=species
    def show(self):
        print("The name of the animal is:", self.name)
        print("The species of the animal is:", self.species)
class Dog(animal):
    def __init__(self,name,bread):
        super().__init__(name,species="Dog")
        self.bread=bread
    def show(self):
        animal.show(self)
        print("Bread is ",self.bread)
class Golden_Retriever(Dog):
    def __init__(self,name,colour):
        super().__init__(name,bread="Golden Retriever")
        self.colour=colour
    def show(self):
        Dog.show(self)
        print("Colour is ",self.colour)

print("\nCalling by Golden_Retriever Class")
a=Golden_Retriever("Shera","Shinny Golden")
a.show()
print("\nCalling by Dog Class")
a=Dog("Shera","Shinny Golden")
a.show()
print("\nCalling by animal Class")
a=animal("Shera","Shinny Golden")
a.show()