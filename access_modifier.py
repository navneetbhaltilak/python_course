class mine:
    def __init__(self):
        self.name="Navneet"
        self.__name="Navneet"  #Here we have added the variable as private
                               #by using (__) 2-underscore as prefix
a=mine()
print(a.name)      #it will be accessed because it is public by default                        
# print(a.__name)  #it can't be accessed like this beacause we have declared
                 #it as a private menber using 2 under_scores as a prefix
print(a._mine__name)  #we have to use this syntax for accessing the private member
                      #<object_name>.<class_name>__<private_member_name>
print(a.__dir__())