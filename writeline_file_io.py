f=open('myfile2.txt','w')
lines=['My Name is Navneet','My Fathers name is Shivajirao','My Surname is Bhaltilak']

for line in lines:
    f.writelines(line +'\n')
f.close()