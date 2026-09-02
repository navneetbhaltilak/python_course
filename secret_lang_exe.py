
a=input("Enter your message : ")
if len(a)>=3:
    # for i in a:
    b=a[1:]+a[0]
    front="e3k"
    back="h7e"
    result =front+b+back
    print(result)
else:
    reverse="".join(reversed(a))
    print(reverse)
choice=input("Want to decode this message : yes/no ")
if choice =='yes':

    if len(a)<3:
        reverse2="".join(reversed(reverse))
        print(reverse2)
    else:
        result2=result[3:-3]
        final=result2[-1]+result2[:-1]
        print(final,"\n--------MessageDecoded----------- ")
else:
    print("\n----------Message Encoded----------")