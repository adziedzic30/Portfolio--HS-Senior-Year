#Name Generator
#Audrey Dziedzic
#10/17/24

#Init

#Functions
print("Welcome to your Fairy Name 2000")
print("Answer the questions to find out your fairy name")
ans = input("cookie (c) or nature (n) ?")
if ans == "c":
    ans = input("chocolatechip (choc) or sugar (sug) ?")
    if ans == "sug":
        ans = input("homemade (home) or crumbl (crumbl) ?")
        if ans == "crumbl":
            print("Your name is Crumb")
        else:
            print("Your name is Homie")
    if ans == "chocolatechip":
        ans = input("panera (pan) or dunkindonuts (dunk) ?")
        if ans == "pan":
            print("Your name is Penny")
        else:
            print("Your name is DoDo")
if ans == "n":
    ans = input("Tree (tre) or Flower (flo) ?")
    if ans == "tre":
        ans = input("Branch (br) or leaf (le) ?")
        if ans == "br":
            print("Your name is Cha Cha")
        else:
            print("Your name is LeLe")
    if ans == "flo":
        ans = input("Dafodill (daf) or Daisy (dai) ?")
        if ans == "daf":
            print("Your name is Daffy")
        else:
            print("Your name is Day Day")

#Main
