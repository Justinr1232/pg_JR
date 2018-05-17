name = "Justin Roldan"

subjects = ["English","Math","Science","Spanish","History"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)

videogames = ["Fortnite", "Rainbow Six Siege", "Call Of Duty", "Halo"]

for i in videogames:
    if i == "Fortnite":
       print(i + " is a 1v1.")
    elif i == "Halo":
        print(i + " is an amazing game.")
    elif i == "Call Of Duty":
        print(i + "is an okay ganme.")
    else:
        print("My favorite video game is " + i)

videogames = []

while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = imput()    

    if answer == "end":
        break
    else:
        videogames.append(answer)

for i in movies:
    print("One of your favorites is " + i)
