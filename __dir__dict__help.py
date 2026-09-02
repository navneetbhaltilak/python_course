class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("Navneet",20)
print(dir(person))   #it is used for knowing thw method you should perform on person
print(p.__dict__)   #it returns the args as a dictionary
print(help(person))  #it give all info of the class(person)