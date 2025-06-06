import random
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
                difficulty()

            elif choice == 2:
                valid = True
                print("ok")
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please input a value inbetween 1-3.")
        except ValueError:
            print("Invalid input. Please input a value inbetween 1-3.")

def difficulty():
    valid = False
    while valid == False:
        try:
            difficulty = int(input("""Choose a difficulty 

1. Easy: 😴 Gives you a line of lyrics which you need to guess within 10 seconds. Hints are enabled which gives you the artist's name. 

2. Avid Listener: ☺️ A little more of a challenge with your lyrics slowly loading in within 5 seconds. 

3. Fanboy: 😅 More challenging than the last two with a different game style. Your lyrics are scrambled around, and you're given 10 seconds to guess what song.  

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
    input("""This version of guess-that-song, you are given a line of lyrics, and you must guess within 10 seconds.
If you wish, you can get a hint which extends the time and gives you the artist's name. However, this does impact your final score

When you’re ready, type any character. """)
    lyrics = ["song 1 lyrics", "song 2 lyrics", "song 3 lyrics", "song 4 lyrics", "song 5 lyrics"]
    song_name = ["1", "2", "3", "4", "5"] 
    indices = random.sample(range(len(lyrics)), len(lyrics))  # Get a shuffled list of indices
    lyrics = [lyrics[i] for i in indices]  
    song_name = [song_name[i] for i in indices]  
    lyrics, song_name = shuffle(lyrics, song_name, random_state = 0) 
    score = 0
    correct = 0
    streak = 0
    x = 1
    print(lyrics)
    print(song_name)
    for num in range(5):
        valid = False
        lyric = lyrics[num]
        guess = input(f"{x}. {lyric}")
        while valid != True:
            if guess == song_name[num]:
                streak += 1
                print(f"Correct! Streak: {streak}")
                x += 1
                score += 10
                correct += 1
                valid = True

            else:
                x += 1
                print("Incorrect!")
                valid = True
                streak = 0
            if streak == 3:
                print("You're on fire!")
        print(f"Score:{score}")
    print(f"Your final score was {score}. You got {correct} out of 5 correct.")

    menu()
    return score
            


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

menu()


# hello blah blah blah

# you are meant to auto commit