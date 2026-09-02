#READING TO A FILE
f=open('myfile.txt','r') #this is use to read the file
text=f.read()
print(text)
f.close()

#WRITING TO A FILE

f=open('myfile2.txt','w')  #it automatically generates if the file is not there
text=f.write("hii") 
f.close()

#APPEND TO A FILE
f=open('myfile2.txt','a')  #it will add the message to the end of the file
text=f.write("hii") 

#USING WITH WHICH WRITE TO AFILE AND CLOSE IT AUTOMATICALLY
with open('myfile.txt','a')as f:
    f.write("Hey,I an Navneet.!")
