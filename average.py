a=list(map(int, input("Enter the numbers seperated with space: ").split()))
def average(*numbers):
  sum=0
  for i in a:
    sum=sum+i
  return sum/len(a)


print(average(*a))