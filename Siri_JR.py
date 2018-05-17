import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb
import pyautogui as pg

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.speak("Hi Justin, what do you want to search for?")
    pg.alert("Listening")
    audio = r.listen(source)
    pg.alert("Thinking")


try:
    words = r.recognize_google(audio)
    speak.speak("Ok Justin, let's look for " + r.recognize_google(audio) + " on Google.")
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    pg.alert("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    pg.alert("Could not request results from Googls Speech Recognition service; {0}" .format(e))
    

