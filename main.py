import random
from colorama import Fore, Back, Style
from sklearn.utils import shuffle


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

            elif choice == 2:
                valid = True
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please input a value inbetween 1-3.")
        except ValueError:
            print("Invalid input. Please input a value inbetween 1-3.")
        return choice
    
def difficulty():
    valid = False
    while valid == False:
        try:
            difficulty_option = int(input("""Choose a difficulty 

1. Easy: 😴 Gives you a line of lyrics which you need to guess within 10 seconds. Hints are enabled which gives you the artist's name. 

2. Avid Listener: ☺️ A little more of a challenge with your lyrics slowly loading in within 5 seconds. 

3. Fanboy: 😅 More challenging than the last two with a different game style. Your lyrics are scrambled around, and you're given 10 seconds to guess what song.  

4. Lyrical Genius: 🤯 For the best of the best, the most challenging of them all. Your lyrics are scrambled, slowly loads in, and you are given 10 seconds to guess the song. 

"""))
            if difficulty_option == 1:
                valid = True
            elif difficulty_option == 2:
                valid = True
            elif difficulty_option == 3:
                valid = True          
            elif difficulty_option == 4:
                valid = True              
            else:
                print("Invalid Input. Please input a value from 1-4.")
        except ValueError:
            print("Invalid Input. Please input a value from 1-4.")
    return difficulty_option
        
def leaderboard(name, score):
    print("""Welcome to the leaderboard
          Here you can view the top 10 people who have scored on this computer.""")

def lyrics_data():
    lyrics = ["You're takin' me out of the ordinary", "If the world was ending, I'd wanna be next to you", "I'm working late, 'cause I'm a singer", "Ain't with my type activities? Then don't you get involved", "And, oh, it's hard to see you, but I wish you were right here"]
    song_name = ["ordinary", "die with a smile", "espresso", "tv off", "love me not"]
    hints = ["Alex Warren", "Bruno Mars and Lady Gaga", "Sabrina Carpenter", "Kendrick Lamar", "Ravyn Lenae"]
    x = random.sample(range(len(lyrics)), len(lyrics))  # Get a shuffled list of indices
    lyrics = [lyrics[i] for i in x]  
    song_name = [song_name[i] for i in x]  # reorded and reassigned back into the list
    return lyrics, song_name, hints

def easy(lyrics, song_name, hints):
    input("""This version of guess-that-song, you are given a line of lyrics, and you must guess within 10 seconds.
If you wish, you can get a hint which extends the time and gives you the artist's name. However, this does impact your final score

When you’re ready, type any character. """)
    
    score = 0
    correct = 0
    streak = 0
    x = 1
    print(lyrics)
    print(song_name)
    for num in range(5):
        valid = False
        lyric = lyrics[num]
        guess = input(f"{x}. {lyric}\n").lower()
        while valid != True:
            if guess == song_name[num]:
                streak += 1
                print(f"{Fore.GREEN}Correct! {Fore.RESET}Streak: {streak}")
                x += 1
                score += 10
                correct += 1
                valid = True
            elif guess == "h":
                print(hints[x])
                guess = input(f"{x}. {lyric}\n").lower()
                score -= 5
                pass
            else:
                x += 1
                print(Fore.RED + "Incorrect!" + Fore.RESET)
                valid = True
                streak = 0
            if streak == 3:
                print("You're on fire!")
        print(f"Score:{score}")
    print(f"Your final score was {score}. You got {correct} out of 5 correct.")
    name = input("Input your name: ")
    menu()
    return score, name
            


def avid():
    input("""This version of guess-that-song, your lyrics load slowly within 5 seconds, and you must guess within 10 seconds. 
The longer it takes you to guess, the lower the score you get. 
If you wish, you can get a hint which extends the time and gives you the artist's name. However, this does impact your final score.  

When you’re ready, type any character. """)
def fanboy():
    input("""This version of guess-that-song, your lyrics are scrambled, and you must guess within 10 seconds. The longer it takes you to guess, the lower the score you get. 
If you wish, you can get a hint which extends the time and gives you the artist's name. However, this does impact your final score.  
          
When you're ready, type any character. """)
def lyrical():
    print("This will be the lyrical genius difficulty")

if __name__ == "__main__":
    choice = menu()
    if choice == 1:
        difficulty()
    elif choice == 2:
        leaderboard()
    difficulty_option = difficulty()
    lyrics, song_name, guess = lyrics_data()
    if difficulty_option == 1:
        easy(lyrics, song_name, guess)

    