#Audrey Dziedzic 11/21/24
#Pokemon Evolution

#Initialize (these are our global variables)
pokemon_level = 0 #Global
pokemon_name = "Squirtle"
day = 1
import random

#Functions
def train():
    global pokemon_level
    global day
    print("Your pokemon just did 10 push ups.")
    pokemon_level = pokemon_level + 1
    print("After day " + str(day) , "your pokemon is at level: ", pokemon_level)
    day = day + 1

def gym_battle():
    global pokemon_level
    global day
    print("Your Squirtle is going to compete in a battle with another Pokemon.")
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        pokemon_level = pokemon_level + 2
        print("Congrats! Your pokemon won and is now at level: ", pokemon_level)
    else:
        print("Sorry, but your pokemon lost and is still at level: ", pokemon_level)
    day = day + 1

def rest():
    global pokemon_level
    global day
    print("Your Pokemon is going to rest.")
    print("After resting, your pokemon is still at level: " + str(pokemon_level))
    print("So it's name is ", pokemon_name)

def evolve():
    global pokemon_level
    global pokemon_name
    if pokemon_level == 0:
        pokemon_name == "Squirtle"
    elif pokemon_level == 2:
        print("Your pokemon has evolved, the new name: Wartortle.")
        pokemon_name = "Wartortle"
    elif pokemon_level == 4:
        print("Your pokemon has evolved, the new name: Blastoise.")
        pokemon_name = "Blastoise"

#Main
print("Welcome to Pokemon Evolution")
while True:
    print("Select an activity for day: " + str(day))
    print("""1.Train
2.Gym Battle
3.Rest(Display info)
4.Quit""")
    activity = int(input("1-4) Activity for the day: "))
    if activity == 1:
        train()
        evolve()
    elif activity == 2:
        gym_battle()
        evolve()
    elif activity == 3:
        rest()
    else:
        break
