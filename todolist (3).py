#Audrey Dziedzic
#To-Do List 1/22/25

#Initialize
themeList = []

#Functions
def makeList():
    print("Welcome to my Theme List Organizer")
    print("Please select one of the following options: ")
    print("1. View \n2. Add \n3. Remove \n4. Quit")

    while True:
        try:
            #Collect User Choice
            option = input("Select a number between 1-4: ")
            option = int(option)

            #Process Information
            if option == 1:
                print("Here is your theme list: ")
                print(themeList)

            if option == 2:
                addItem = input("What would you list to add to your list?")
                themeList.append(addItem)
                print("Successfully added " + addItem)

            if option == 3:
                removeItem = input("What would you list to remove from your list?")
                themeList.remove(removeItem)
                print("Successfully removed " + removeItem)

            if option == 4:
                print("Thanks for letting me make your list.")
                break
        except:
            print("ERROR: Please enter a number!!")

#Main
makeList()
