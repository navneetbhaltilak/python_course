import random
def check_win(player,computer):
    if(player==computer):
        return "It's a tie"
    elif(player=="snake" and computer=="water")\
    or(player=="water" and computer =="gun")\
    or(player=="snake" and computer =="water"):
        return "You Win!"
    else:
        return "Computer Wins!"
def play_game():
    choices=["snake","gun","water"]
    player=input("Enter your choice(snake/gun/water) : ").lower()

    if player not in choices:
        return "Invalid choice! please pick from snake,gun or water."
    computer=random.choice(choices)
    print(f"Computer's choice : {computer}")
    result=check_win(player,computer)
    return result
print(play_game())