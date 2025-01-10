#Audrey Dziedzic
#1/6/25
#Rock Paper Sicssors

#Init
import random
player_score = 0 #Global
computer_score = 0 #Global

#Functions
def game():
    global player_score
    global computer_score
    print("Welcome to the Rock, Paper, Scissors Game!")
    while True:
        #Player's choice
        print("Please select one of the three options.")
        player = input("Selection (rock or paper or scissors):")
        #Computer's Choice
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("The computer chose rock")
        elif computer == 2:
            computer = "paper"
            print("The computer chose paper")
        else:
            computer = "scissors"
            print("The computer chose scissors")
        #Determine the outcome
        if player == "rock" and computer == "scissors":
            player_score = player_score + 1
            computer_score = computer_score
            print("You won")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "rock" and computer == "paper":
            player_score = player_score
            computer_score = computer_score + 1
            print("You lost")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "rock" and computer == "rock":
            player_score = player_score
            computer_score = computer_score
            print("Tie")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "paper" and computer == "scissors":
            player_score = player_score
            computer_score = computer_score + 1
            print("You lost")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "paper" and computer == "paper":
            player_score = player_score
            computer_score = computer_score
            print("Tie")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "paper" and computer == "rock":
            player_score = player_score + 1
            computer_score = computer_score
            print("You won")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "scissors" and computer == "scissors":
            player_score = player_score
            computer_score = computer_score
            print("Tie")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "scissors" and computer == "rock":
            player_score = player_score
            computer_score = computer_score + 1
            print("You lost")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        elif player == "scissors" and computer == "paper":
            player_score = player_score + 1
            computer_score = computer_score
            print("You won")
            print("You have" ,player_score, "points and the computer has" , computer_score)
        #Ask player if they want to continue
        playagain = input("Would you like to play again?")
        if playagain == "yes":
            print("Restarting...")
        elif playagain == "no":
            print("Ok, thanks for playing.")
            break

#Main
game()
