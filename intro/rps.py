from traceback import print_tb


import random as ran
move = ran.randint(0,2)

print('Rock...')
print('Paper...')
print('Scissors..')

if move == 0:
    computer = "rock"
elif move == 1:
    computer = "paper"
else:
    computer = "scissors"


player1 = input("Player one: ")
print(f"Computer: {computer}")

if player1 == computer:
    print("it's a tie")
elif player1 == "rock":
        if computer == "scissors":
            print("player 1 WINS")
        if computer == "paper":
            print("computer wins") 
elif player1 =="paper":
        if computer == "rock":
            print("player one wins")
        if computer == "scissors":
            print("computer wins")
elif player1 == "scissors":
        if computer == "paper":
            print("Player one wins")
        if computer == "rock":
            print("computer wins")
else:
    print("You broke it. Good Job!")