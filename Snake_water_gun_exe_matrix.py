import random
def play_game():
        choices=["gun","snake","water"]
        outcomes=[
            [0, 1, -1],
            [-1, 0, 1],
            [1, -1, 0]
        ]
        player=input("Enter your choice(snake/gun/water) : ").lower()
        if player not in choices:
            return "Invalid Choice ! Please choose from snake,gun or water." 
        computer = random.choice(choices) 
        print(f"Computer Chooses : {computer}")
        
        player_index=choices.index(player)
        computer_index=choices.index(computer)
        result=outcomes[player_index][computer_index]
        if result==0:
              print("It's a tie!") 
              return print(play_game())
        elif result==1:
              print("You Win!")
              return print(play_game())
        else:
              print("Computer Wins!")
              return print(play_game())
print(play_game())