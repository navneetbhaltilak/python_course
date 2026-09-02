import time
c=str(input("Enter your name ="))

t=time.strftime('%H,%M,%S')
a=int(time.strftime('%H'))
b=int(time.strftime('%M'))
print("Time is :- ",a,':',b)
if(6<=a<=11 and 0<=b<=59 ) :
  print("Good Morning Mr.",c)
elif (17>=a>=12 and 59>=b>=0 ):
    print("Good Afteernoon Mr.",c)
elif(19>=a>=18 and 59>=b>=0 ):
      print("Good Eveningn Mr.",c)
elif (23>=a>=20 and 59>=b>=0) :
      print("Good Night Mr.",c)

else :
  print("invalid")