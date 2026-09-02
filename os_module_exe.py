import os
print("Current Directory : ",os.getcwd())
new_dir=input("Paste the folder address you want to use : ")
os.chdir(new_dir)
print("Now the new directory: ",os.getcwd())
files=os.listdir(new_dir)
i = 1
b=input("Enter name you want to give : ")
a=int(input("Want to change \nPress-1(Yes) \nPress-0(No)\n"))
for file in files:
    if file.endswith(".py"):
        if a==1:
            os.rename(f"{new_dir}/{file}",f"{new_dir}/{b}-{i}.png")
            i=i+1
        elif a==0:
            print("Operation Unsuccessfull...")
        else:
            print("Invalid Operation..")
        