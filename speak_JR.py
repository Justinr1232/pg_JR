import win32com.client as wincl
import webbrowser as wb
import pyautogui as pg

speak = wincl.Dispatch("SAPI.SpVoice")

speak.speak("What is your name?")
answer = pg.prompt("Enter your name.")

speak.speak("hello " + answer + "How was your day?")
day = pg.prompt("Enter how your day was.")

if day == "Great":
    speak.speak("Im glad to hear that!")

elif day == "Bad":
    speak.speak("What could make your day better?")
    better = pg.prompt("Enter what could make your day better?")
    speak.speak("I hope " + better + "makes your day better.")



else:
    speak.speak("It's was great to see you!")

speak.speak("What kind of video would you like to watch?")
video = pg.prompt("Enter video to watch")
speak.speak("Ok, you want to watch videos about " + video)

wb.open("https://www.youtube.com/results?search_query=" + video)
                   
