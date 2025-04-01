# testing
def menu():
    valid = False
    while valid == False:
        try:
            choice = int(input("""Welcome to 🎤 Guess-that-song! 🎤
1. Play ▶️ 
2. Leaderboard 🏅 
3. Quit 👋
"""))
        except ValueError:
            print("Invalid input. Please input a value inbetween 1-3.")

        if choice == 1:
            valid = True
            print("ok")

        elif choice == 2:
            valid = True
            print("ok")
        else:
            quit

menu()

# hello blah blah blah

# you are meant to auto commit