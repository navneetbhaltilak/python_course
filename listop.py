list=[1,2,3,4,5,"navneet","yogita","eshant","harsh","ashish","rachi"]
#define the length of a list
print(len(list))
#running simple list operations
print(list [1:7])
print(list [:5])
print(list [0:])
#running an jump index operations
print(list [0:9:2])
print(list [::2])
#running operation on negative index
print(list [1:-7])
print(list [3:-1])
print(list [10])
print(list [-2:-1:2])
#running an negative jump index operations 
print(list [-1:-7:-2])
print(list [-1:])
print(list[:-9])
#running an comperhensive list operations
list=[i for i in range(4)]
print(list)
list=[i*i for i in range(4)]
print(list)
list=[i*i for i in range(10)]
print(list)
list=[i*i for i in range(10) if i%2==0]
print(list)