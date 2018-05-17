import pyautogui as pg
import webbrowser
import time

answer = pg.confirm(text="How would you describe your stress level at this moment? (1 is very little stress. 10 is high stress levels)", title= "Stress Level", buttons=['1,2,3', '4,5,6', '7,8,9,10'])
    
if answer == "1,2,3":
    answer = pg.prompt(
        """
 What has made your day well so far?
 """)
    
    pg.alert("Keep on having a nice day!") 
    webbrowser.open("https://www.youtube.com/watch?v=1ZYbU82GVz4") 



if answer == "4,5,6":
    answer = pg.prompt(
        """
What could make your day better?
""")

    if "dogs" in answer:
        pg.alert("Enjoy these videos about dogs")
    elif "cats" in answer:
        pg.alert("Enjoy these videos about cats")
    else:
        

    
    pg.alert("I hope you enjoy " + answer)
    pg.alert("Here's a fun video to keep you smiling!")
    webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")


elif answer == "7,8,9,10":
    answer = pg.prompt(
        """
I'm sorry you're stressed . Any particular reason?

""")
    pg.alert("I hope this will make you feel better.")
    webbrowser.open("https://www.youtube.com/watch?v=MBRqu0YOH14")    
