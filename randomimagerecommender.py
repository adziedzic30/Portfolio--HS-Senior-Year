#Audrey Dziedzic 2/24/25
#Random Image Recommender

#Init
from PIL import Image
import requests
from io import BytesIO
import random

#List of Desserts
dessertList = ["https://tinyurl.com/58rtmsp6" , #Berry Tart
               "https://tinyurl.com/yc7mpk5v" , #Macaroons
               "https://tinyurl.com/yx4fx8ab" , #Pie
               "https://tinyurl.com/bdeh42u7" , #Ice cream
               "https://tinyurl.com/5n6aejut"] #Cupcake

#Functions
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

#Main
def randomrecommender():
    print("Welcome to the dessert recommendation app.")
    question = input("Do you want your recoomendation (y/n)?")
    recommend = random.choice(dessertList)
    if question == "y":
            if recommend == "https://tinyurl.com/58rtmsp6":
                print("This is a berry tart. This has fruits in it so if you like fruits it is good. Also, it might be a little healthier for a dessert.")
            elif recommend == "https://tinyurl.com/yc7mpk5v":
                print("This is a macaroon which are originally from France. They are very expensive usually because they are so hard to make, but have a unique texture.")
            elif recommend == "https://tinyurl.com/yx4fx8ab":
                print("This is a pie. Pies are good for a holiday like for Thanksgiving you may want a pumpkin pie and in the spring, maybe you want an apple pie. ")
            elif recommend == "https://tinyurl.com/bdeh42u7":
                print("This is ice cream, which is nice during the summer if it a hot day because it is cold. You can get it on a cone or in a bowl.")
            else:
                print("This is a cupcake. This is good because you can hold it in your hand and don't need a fork to eat it. It comes in a lot of flavors too.")
            open_image(recommend)
    else:
            print("Ok.")

randomrecommender()

#Sources
#The berry tart image was found at the Playing With Flour website (http://www.playingwithflour.com/2012/05/mini-fruit-tarts-for-moms.html) by Monica on March 13th, 2019
#The macaroon image was found at the Free Dessert Photos website (https://www.pexels.com/search/dessert/) by an unkwon use and date
#The pie image was found at the recipes.com website (https://recipepes.com/indx.html?utm_content=savory+pie+recipes) by y.e.ygt@hotmail.com in 2024
#The ice cream image was found at the H-O-M-E webiste (https://h-o-m-e.org/does-ice-cream-have-eggs/) by William Armstrong on an unknown date
#The cupcake image was found at The Busy Baker website (https://thebusybaker.ca/best-ever-chocolate-cupcakes-from-scratch/) by Chrissie on 12/19/23
