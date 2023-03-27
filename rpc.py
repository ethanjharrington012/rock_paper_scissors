# rock_paper_scissors

# 'player'
# 'computer'

# first action: computer - random pick ['rock', 'paper', 'scissors']
# second action: player - pick ['rock', 'paper', 'scissors']

# outcome:  -'Game Tied'
#           -'You Win'
#           -'You Loose'

# collect input until 'I quit'
# print 'Thank you for playing!'
import random

def rock_paper_scissors():
    while True:
        options = ['rock', 'paper', 'scissors']
        computer = random.choice(options)
        first_q = input("\nWould you wanna play? [y/n]: ")
        if first_q == "n":
            break
        player = input("\nPick rock[r] paper[p] scissors[s]: ")
        if player == computer:
            print("\nGame tied")
        elif computer == 'rock' and player =='s':
            print("\nComputer wins!")
        elif computer == 'rock' and player == 'p':
            print("\nplayer wins")
        elif computer == 'rock' and player == 'r':
            print("\nTied")
        elif computer == 'scissors' and player == 'r':
            print('\nplayer wins')
        elif computer == 'scissors' and player == 'p':
            print("\ncomputer wins")
        elif computer == 'scissors' and player == 's':
            print("\ntied")
        elif computer == 'paper' and player == 's':
            print("\nplayer wins")
        elif computer == 'paper' and player == 'r':
            print("\ncomputer wins")
        elif computer == "paper" and player == 'p':
            print("\nTied")
        else:
            print("I didn't know there was other options you silly goose")
            continue
            
        print(f"\nYou chose {player.title()},  A.I. chose {computer.upper()}")
    
print(rock_paper_scissors())