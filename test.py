import random

choices = ['Rock', 'Paper', 'Scissors ']

class RPS():
    
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        self.computer_choice = random.choice(choices)
        return self.computer_choice

    def get_user_choice(self):
        self.user_choice = input("Do you choose Rock, Paper or Scissors?: ")
        return self.user_choice

    def get_winner(self,computer_choice, user_choice):
        print(f"You chose {self.user_choice} and the Computer chose {self.computer_choice}")
        if computer_choice == user_choice:
                print ("You Draw!")
        elif (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Scissors' and user_choice == 'Rock') or (computer_choice == 'Paper' and user_choice == 'Scissors'):
                print("You win!")
                self.user_wins +=1
        elif (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
                print("The computer wins!")
                self.computer_wins +=1

def play():
    game = RPS()

    while game.user_wins < 3 or game.computer_wins < 3:
        computer_choice = game.get_computer_choice
        user_choice = game.get_user_choice
        game.get_winner(computer_choice, user_choice)

        if game.user_wins == 3:
            break
        else: 
            game.computer_wins == 3
            break


play()

