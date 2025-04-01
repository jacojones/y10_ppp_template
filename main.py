# testing
from random import randint
from random import shuffle
def menu():
    valid = False
    while valid == False:
        try:
            choice = int(input("""Welcome to 🎤 Guess-that-song! 🎤
1. Play ▶️ 
2. Leaderboard 🏅 
3. Quit 👋
"""))
            if choice == 1:
                valid = True
                difficulty()

            elif choice == 2:
                valid = True
                print("ok")
            elif choice == 3:
                quit
            else:
                print("Invalid input. Please input a value inbetween 1-3.")
        except ValueError:
            print("Invalid input. Please input a value inbetween 1-3.")

def difficulty():
    valid = False
    while valid == False:
        try:
            difficulty = int(input("""Choose a difficulty 

1. Easy: 😴 gives you a line of lyrics which you need to guess within 10 seconds. Hints are enabled which gives you the artist's name. 

2. Avid Listener: ☺️ A little more of a challenge with your lyrics slowly loading in within 5 seconds. 

3. Fanboy: 😅 More challenging than the last two with a different game style. Your lyrics are scrambled around, and you’re given 10 seconds to guess what song.  

4. Lyrical Genius: 🤯 For the best of the best, the most challenging of them all. Your lyrics are scrambled, slowly loads in, and you are given 10 seconds to guess the song. 

"""))
            if difficulty == 1:
                valid = True
                easy()
            elif difficulty == 2:
                valid = True
                avid()
            elif difficulty == 3:
                valid = True          
                fanboy()
            elif difficulty == 4:
                valid = True              
                lyrical()
            else:
                print("Invalid Input. Please input a value from 1-4.")
        except ValueError:
            print("Invalid Input. Please input a value from 1-4.")


def easy():
    print("This is the easy difficulty")
def avid():
    print("This will be the avid-listener difficulty")
def fanboy():
    print("This will be the fanboy difficulty")
def lyrical():
    print("This will be the lyrical genius difficulty")

menu()
# hello blah blah blah

# you are meant to auto commit