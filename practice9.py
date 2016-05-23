import random

class guessing_game_one:
    play = True
    this_round = True
    while play == True:
        a = random.randint(1, 26)
        if this_round == True:
            while this_round == True:
                guess = int(input("Please enter a guess from 1 to 25, inclusive."))
                if a == guess:
                    print("You've guessed correctly.")
                    this_round = False
                elif guess < a:
                    print("Your guess is too low.")
                elif guess > a:
                    print("Your guess is too high.")
                else:
                    print("Try again.")
        elif this_round == False:
            continue_game = input("Continue playing? (Y/N)")
            if continue_game == "N":
                play = False
            elif continue_game == "Y":
                this_round = True
                play = True