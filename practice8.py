class rock_paper_scissors:
    score1 = 0
    score2 = 0
    print()
    print("Rock, paper, scissors, best two out of three.")

    while score1 < 2 and score2 < 2:
        print()
        player1 = int(input("Choose 1) Rock, 2) Paper or 3) Scissors: "))
        player2 = int(input("Choose 1) Rock, 2) Paper or 3) Scissors: "))
        if player1 == player2:
            print("tie")
        elif player1 == 1:
            if player2 == 2:
                print("Paper covers Rock, Player 2 wins")
                score2 += 1
            elif player2 == 3:
                print("Rock crushes Scissors, Player 1 wins.")
                score1 += 1
        elif player1 == 2:
            if player2 == 1:
                print("Paper covers Rock, Player 1 wins")
                score1 += 1
            elif player2 == 3:
                print("Scissors cuts Paper, Player 2 wins.")
                score2 += 1
        elif player1 == 3:
            if player2 == 1:
                print("Rock crushes Scissors, Player 2 wins.")
                score2 += 1
            elif player2 == 2:
                print("Scissors cuts Paper, Player 1 wins.")
                score1 += 1

    if score1 == 2:
        print("Player 1 wins.")
        score1 += 1
    elif score2 == 2:
        print("Player 2 wins.")
        score2 += 1