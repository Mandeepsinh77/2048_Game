import random #bring in the random number
import time
number=random.randint(1, 100) #pick the number between 1 and 200

def introduction():
    print("May I ask you for your name?")
    name=input() #asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6: #if the number of guesses is less than 6
        time.sleep(.25)
        enter=input("Guess: ") #inserts the place to enter guess
        try: #check if a number was entered
            guess = int(enter) #stores the guess as an integer instead of a string    

            if guess<=100 and guess>=1: #if they are in range
                guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number that you have entered is  low")
                    if guess>number:
                        print("The guess of the number that you have entered is  high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess==number:
                    break #if the guess is right, then we are going to jump out of the while block
            if guess>100 or guess<1: #if they aren't in the range
                print("That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")

        except: #if a number wasn't entered
            print("I don't think that "+enter+" is a number. Sorry")
            
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    introduction()
    pick()
    print("Do you want to play again?")
    playagain=input()