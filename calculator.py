print("*************CALCULATOR*************")
a=int(input("\nEnter first number = "))
c=input("\nEnter the sign = ")
b=int(input("\nEnter second number = "))

if c =='+':
   print("\nThe addition of two number is = ", a + b)
elif c =='-':
   print("\nThe substraction of two number is = ",a-b)
elif c =='/':
    print("\nThe division of two number is = ",a/b)
elif c =='%':
    print("\nThe modulus of two number is = ",a%b)
elif c =='//':
    print("\nThe float division of two number is = ",a//b)
elif c =='**':
    print("\nThe exponential of two number is = ",a**b)
elif c =='*':
    print("\nThe multiplication of two number is = ",a*b)
else:
    print('please enter operator')
