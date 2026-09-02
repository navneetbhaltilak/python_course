#Ye hai aam, zindagi without walrus(:=) operator
'''
food=list()
while True:
    item=input("Which food do you like ? --> ")
    if item=="quit":
        break
    food.append(item)
print(food)
'''
#abhi dekho Mentos zindagi woth walrus operator(:=)\
food=list()
while (item:=input("Which food do you like ?--->"))!="quit":
    food.append(item)
print(food)