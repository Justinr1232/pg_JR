import pyautogui as pg
import time

import webbrowser
points = 0

# Question

answer = pg.prompt(
"""
What way do you like to breach?

a) Take a slow approach
b) Break a barrior to get in
c) Make a hole and rush
d) Drone it out and then walk in 

"""

    )

# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4


# Question 2

answer = pg.prompt(
"""
What do you prefer?

a) Semi-auto Rifle 
b) Full Auto Rifle 
c) LMG
d) Hard-hitting Gun 

"""

    )

# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4



    # Question 3

answer = pg.prompt(
"""
Who would you choose?

a) Buck
b) Backbeard
c) Hibana
d) Capitao

"""

    )

# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4



# END OF SURVEY

pg.alert("You Are...")

# Blackbeard
if points < 6:
    pg.alert("Blackbeard")
    webbrowser.open("http://vignette2.wikia.nocookie.net/rainbowsix/images/a/a1/Blackbeard.jpg/revision/latest?cb=20160512173157")

# Buck
elif points >= 6 and points < 9:
    pg. alert ("Buck")
    webbrowser.open("https://res.cloudinary.com/pvplive/image/upload/article_headers/RS-20170418-Bundle.jpg")

# Hibana
elif points >= 9 and points <11:
    pg.alert ("Hibana")
    webbrowser.open("https://ubistatic19-a.akamaihd.net/resource/en-us/game/rainbow6/siege/r6-operators-hibana_275606.png")

# Capitao
elif points >=11:
    pg.alert ("Capitao")
    webbrowser.open("https://steamuserimages-a.akamaihd.net/ugc/858360646832951063/18850C7FC8D2FD825D31BB148EA2312EEECE4F0E/")

