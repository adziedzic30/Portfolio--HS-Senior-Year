#Audrey Dziedzic 1/8/25
#Multiplication Quiz

#Init
import random
import time

#Functions
def quiz():
    global score
    score = 0
    print("Welcome to the multiplication quiz!")
    print("How many questions would you like the quiz to be?")
    length = int(input("Enter the number of questions you want:"))
    start_time = time.time()
    for i in range (length):
        computerone = random.randint(0,10)
        computertwo =  random.randint(0,10)
        print("What is",str(computerone),"times",str(computertwo),"?")
        answer = int(input("Enter what you think that answer is:"))
        print("Your answer:", str(answer))
        correctanswer = (computerone*computertwo)
        if answer == correctanswer:
            print("That is correct!")
            score = score + 1
        else:
            print("That is wrong.")
            score = score
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("You finsished the quiz. You got", str(score), "correct out of", str(length))
    print("It took you",str(elapsed_time), "seconds.")

#Main
quiz()
