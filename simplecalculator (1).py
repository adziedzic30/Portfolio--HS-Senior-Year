#Simple Calculator
#Audrey Dziedzic 11/19/24

#Init

#Function
#Adds num1 and num2 and prints the result
def add(num1,num2):
    result = num1 + num2 #Or print(num1+num2)
    print(result)

def subtraction(num1, num2):
    result = num1 - num2
    print(result)

def division(num1, num2):
    result = num1 / num2
    print(result)

def multiplication(num1, num2):
    result = num1 * num2
    print(result)

def simplecalc():
    print("Welcome Preschoolers to Simple Calculator")
while True:
    print("Enter an operation (1-5): ")
    print("""1.Addition
2.Subtraction
3.Division
4.Multiplication
5.Quit""")
    operation = int(input("(1-5)Operation: "))
    if operation == 1: #True
        int1 = input("Enter your first number: ")
        int2 = input("Enter your second number: ")
        su = int(int1) + int(int2)
        print(su)

    if operation == 2: #True
        int1 = input("Enter the number you want to subtract from: ")
        int2 = input("Enter the amount to subtract: ")
        sub = int(int1) - int(int2)
        print(sub)

    if operation == 3: #True
        int1 = input("Enter your dividend: ")
        int2 = input("Enter your divisor: ")
        div = int(int1) / int(int2)
        print(div)

    if operation == 4: #True
        int1 = input("Enter your first number: ")
        int2 = input("Enter your second number: ")
        mult = int(int1) * int(int2)
        print(mult)

    if operation == 5:
        break
#Main
simplecalc()
