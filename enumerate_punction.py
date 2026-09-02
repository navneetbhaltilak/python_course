marks = [12,11,34,45,6,7,8,90]
colours = ['green','red','purple']
# index=0
# for mark in marks:
#     print(mark)
#     if(index==7):
#         print("Awesome, Navneet")
#     index +=1


# here with the help of following syntax we ka access any list ,tupple, dic,etc
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index ==7):
        print("Awesome Navneet!")

for index,colour in enumerate(colours,start=1):
    print(index,colour)
    if(index==2):
        print("Its my Favourite colour")