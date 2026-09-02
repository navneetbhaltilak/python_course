import math
#here we have to create a small function 
#the regular way is: 
def double(x):
    return x*2
print(f"double with the help of regular def : {double(5)}")

def cube(x):
    return x*x*x
print(f"cube with the help of regular def : {cube(5)}")

def avg(x,y):
    return (x+y)/2
print(f"Average with the help of regular def : {avg(5,6)}")

# we can also use function(func) but the func should be present in your file
def apply(func,value):
    return func(value)
print(f"Function(func) in function(apply) with the help of regular def : {apply(cube,6)}")

#Now using lambda function
double = lambda x: x*2
cube = lambda x: x*x*x
print(f"double with the help of lambda function : {double(5)}")
print(f"cube with the help of lambda function : {cube(5)}")

#It can also take 2 or more values in a single line
avg =lambda x,y:(x+y)/2
print(f"more than 2 value with the help of lambda function : {avg(5,6)}")

# we can also use function(func) but the func should be present in your file or use lambda anonymously
print(f"Function(func) in function(apply) with the help of lambda : {apply(lambda x:math.sqrt(x),4)}")
