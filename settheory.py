ns={1,2,1,3,4,3,}
s={1,2,5,6,5,7,8,7,}
print(ns.union(s))
#to add more then one element in a existing string
ns.update(s)
print(ns)
#for finding is the string contain the same elements
print(ns.intersection(s))
sn=ns.intersection_update(s)
print(sn)
#symmetric difference which removes the same values of both sets
sn1=(ns.symmetric_difference(s))
print(sn1)
# some simple operations of string
print(ns.isdisjoint(s))
print(ns.issubset(s))
print(ns.issuperset(s))
# to add a single element
ns.add(9)
print(ns)
#to remove something
ns.remove(9)
print(ns)
#agar koi element set main present na ho aur fir bhi app use discrad karoge toh aapko error nhi milega
ns.discard(11)
#remove gives an error
# ns.remove(11)
# to get some element for string
item=ns.pop()
print(item)
#to delete a set
del (sn)
#for clearing a set
sn1.clear()
print(sn1)