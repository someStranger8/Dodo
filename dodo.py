#python 3.7.1
import time
import random
import math
import sys
print("DODO")
print("--------------------")
time.sleep(1)
print("Welcome to Dodo. Dodo is a tool to help inprove password cracking skills for pen-testers.")
time.sleep(1)
print("Dodo generates a random passward for you to solve.")
time.sleep(1)
print("There are 50+ passwords that it can generate. Hint: all the passwards are 8 digits")
time.sleep(1)
pacote = ["12345678","45739786","13735469","25340987","36458675","34277564","46578675","01928374","45367869","65923856","38745602","38472356","47362945","56479283","56476473","56471945","46574235","46287364","37461928","47569283","64539210","54638219","65749210","74836574","92746592","65920138","75649201","74560192","65748329","75649210","46359784","45369789","65473547","46398462","65924665","99999999","00000000","11111111","75640129","56835623","09876543","46375394","36475968","10298347","47382910","29381029","56293810","46572378","45367869","35269780","45362718","82371029","56473829","29564738","49838645"]
game = random.choice(pacote)
i = 1
while i < 6:
    password=input("Whats the password")
    if password == "{}".format(game):
        print("Congrats! Now try agian and keep practicing")
        time.sleep(20)
        sys.exit()
    else:
        print("sorry try agian")
        time.sleep(1)
i += 1