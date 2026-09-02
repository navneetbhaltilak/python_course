#MAP
def cube(x):
    return x*x*x
#if i want to perform action on every element in a list 
#normal way
l=[1,2,3,4,5,6]
newl=[]
for item in l:
    newl.append(cube(item))
print("Output in normal way operation in list : ",newl)

#with the help of map
newl=list(map(cube,l))
print("Output with using map function in a list : ",newl)

#FILTER
def filter_function(x):
    if x>2:
        return x
newl=list(filter(filter_function,l))
print("Output using filter function : ",newl)

# we cannot do it with the help of for loop because it will return true false value
print("Output with using for loop for\nfilterring each element in a list : ",list(filter_function(item)for item in l))
