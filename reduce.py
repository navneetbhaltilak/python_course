import functools as f  #for using reduce we have to import it 
number=[1,2,3,4,5]
print("The sum is : ",f.reduce(lambda x,y:x+y,number))