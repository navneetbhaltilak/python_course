#to import and of the libraries like math U can use this
import math    
result=math.sqrt(49)
print(result)

# If you want to import math as something so that you dont have to call math every 
# time while using its func then you should do this
import math as m
result=m.sqrt(49)
print("With using 'as'",result)

# If you want to import only the needed function
from math import sqrt,pi
result = sqrt(49)*pi
print("By using from and importing only sqrt and pi from math ",result)