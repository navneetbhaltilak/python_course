y=3
x=9   #this is a global variable
def my_func():  #defined a function
    global x #if you want to use a global value of x then you have to use this
    y=2
    x=5      #this is a local variable
    print("y : ",y,"\nx : ",x)
print("The value of x globally : ",x)# ye hame x ki global value deka kyu ki function ne abhi tak kuch change nhi kiya hai
my_func()
print("The value of x after the function overwrite it : ",x)  # global x ne x ki global value ko overwrite kar diya function mai
print("the value of y globally : ",y)