questions=[ 
 [
     "Which of the following countries is the world's largest producer of saffron?","Spain","Iran","India","Greece",2
 ],
 [
     "Which god is also known as 'Gauri Nandan'?",'Ganesha','Hanuman','Agni','Indra',1
 ],
 [
  'What does not grow on tree according to a popular Hindi saying?','Money','Fruits','Leaves','Flowers',1
 ],
 [
    'Which city is known as the pink city of india?','Jaipur','Kochi','Maysore','Banglore',1
 ],
 [
    "Who wrote India's National Anthem?",'Lal Bahadur Shastri','Rabindranath Tagore','Chetan Bhagat','RK Narayan',2
 ],
]
levels =[1000,2000,4000,8000,16000,32000]
money =0
for i in range(len(questions)):
    #divide the list
    q = questions[i]
    answer=None
    print(f"\n\nQuestions for Rs.{levels[i]}:")
    print(q[0])
    print(f"a.{q[1]}          b.{q[2]}")
    print(f"c.{q[3]}          d.{q[4]}")
    reply =input("select your answer for the given options(a,b,c,d) or enter '0' to quit :- ")
    if reply == 'a':
        answer=1
    elif reply == 'b':
        answer=2
    elif reply == 'c':
        answer=3
    elif reply == 'd':
        answer=4
    elif reply == '0':
        print("Better Luck Next Time")
        break
    else:
        print("Invalid input")
    
    if answer==q[5]:
        print(f"Absolutely correct answer! Congratulation! You won Rs.{levels[i]}")
        if i==1:
            money=1000
        elif i==2:
            money=2000
        elif i==3:
            money=4000
        elif i==4:
            money=8000
        elif i==5:
            money=16000
    else:
        print("OOP's Wrong Answer")
print(f"Money that you can take home in {money*2}")


