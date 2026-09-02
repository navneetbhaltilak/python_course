import random
import string
message=input("Enter your message : ")
words =message.split(" ")
coding=input("1-for coding or 0-for decoding \n")
def random_str(length=3):
    return''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length))

coding =True if(coding=="1") else False
if(coding):
    string_list=[]
    for word in words:
        if(len(word)>=3):
            en_msg=random_str(3)+word[1:]+word[0]+random_str(3)
            string_list.append(en_msg)
        else:
            # reverse="".join(reversed(i))
            string_list.append(word[::-1])
    print(" ".join(string_list))
else:
    string_list=[]
    for word in words:
        if(len(word)>=3):
            en_msg=word[3:-3]
            en_msg=en_msg[-1]+en_msg[:-1]
            string_list.append(en_msg)
        else:
            # reverse="".join(reversed(i))
            string_list.append(word[::-1])
    print(" ".join(string_list))