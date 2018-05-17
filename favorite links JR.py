import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=xjDjIWPwcPU","https://www.youtube.com/watch?v=6ZfuNTqbHE8"]

music = ["https://www.spotify.com/us/","https://www.youtube.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch videos
b) listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
