import random

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    print("guess my number between 1 and 100!")
    guess = int(input())

    counter += 1

    if guess == number:
        print("You deserve a coockie")
        print("yOU tried " + str(counter) + "gueses")
        break

    elif guess > number:
        print("Too high, try again.")

    elif guess < number:
        print("Too low, try again.")

    
