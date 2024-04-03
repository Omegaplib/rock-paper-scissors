def rock_paper_scissors():
    hands = ['rock', 'paper', 'scissors']

    player_1 = input("What hand are you playing?: ").lower()
    player_2 = input("What is your opponent's hand?: ").lower()

    if player_1 and player_2 in hands:
        if player_1 == 'rock' and player_2 == 'scissors' or player_1 == 'paper' and player_2 == 'rock' or player_1 == 'scissors' and player_2 == 'paper':
            print(f"Player 1 wins because {player_1} beats {player_2}")
        elif player_2 == 'rock' and player_1 == 'scissors' or player_2 == 'paper' and player_1 == 'rock' or player_2 == 'scissors' and player_1 == 'paper':
            print(f"Player 2 wins because {player_2} beats {player_1}")
        elif player_1 == player_2:
            print(f"It's a draw!")
    else:
        print("Invalid inputs")

if __name__ == '__main__':
    rock_paper_scissors()

