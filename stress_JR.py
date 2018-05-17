import pyautogui as pg
import webbrowser
import time

answer = pg.confirm(text="How would you describe your stress level at this moment?", title= "Stress Level", buttons=['1,2,3', '4,5,6', '7,8,9,10'])
    
if answer == "1,2,3":
    pg.alert("https://www.youtube.com/watch?v=OG2eGVt6v2o") 



if answer == "4,5,6":
    answer = pg.confirm(
        """
Glad to hear you're happy! What are you up to today?
""")
    pg.alert("I hope you enjoy: " + answer)
    pg.alert("Here's a fun video to keep you smiling!")
    webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")


elif  == "b":
    answer = pg.confirm(
        """
I'm sorry you're sad. Any particular reason?

""")
    pg.alert("I hope this will make you feel a little better.")
    webbrowser.open("https://www.youtube.com/watch?v=MBRqu0YOH14")    
