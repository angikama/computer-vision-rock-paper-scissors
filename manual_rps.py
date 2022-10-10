import random

class RPS():

    def __init__(self):
        self.actions = ["R","P","S"]

# randomly choses an action for the computer      
    def get_computer_choice(self):
        self.computer_choice = random.choice(self.actions)
        if self.computer_choice == "R":
            self.computer_choice_name = "Rock"
        elif self.computer_choice == "P":
            self.computer_choice_name = "Paper"
        else:
            self.computer_choice == "S"
            self.computer_choice_name = "Scissors"

        return self.computer_choice

# gets input from the user
    def get_user_choice(self):
        self.user_choice = input("Do you choose Rock(R), Paper(P) or Scissors(S)? ").upper()
        if self.user_choice == "R":
            self.user_choice_name = "Rock"
        elif self.user_choice == "P":
            self.user_choice_name = "Paper"
        else:
            self.user_choice == "S"
            self.user_choice_name = "Scissors"
        return self.user_choice

# decides who wins
    def get_winner(self,computer_choice, user_choice, computer_choice_name, user_choice_name):
        print(f"You chose {user_choice_name} and the Computer chose {computer_choice_name}")
        while True:
            if computer_choice == user_choice:
                 print ("You Draw!")
            elif computer_choice == "R" and user_choice == "P":
                print("You win!")
            elif computer_choice == "R" and user_choice == "S":
                print("The computer wins!")
            elif computer_choice == "P" and user_choice == "R":
                print("The computer wins")
            elif computer_choice == "P" and user_choice == "S":
                print("You win!")
            elif computer_choice == "S" and user_choice == "R":
                    print("You win!")
            else:
                computer_choice == "S" and user_choice == "P"
                print("The computer wins!")
                
            play_again = input("Do you want to play again? (y/n) : ")
            if play_again.lower() == "y":
                play()
            else: 
                play_again.lower() == "n"
                break
                
        

def play():
    game = RPS()
    computer_choice = game.get_computer_choice()
    user_choice = game.get_user_choice()
    computer_choice_name = game.computer_choice_name
    user_choice_name = game.user_choice_name
    game.get_winner(computer_choice, user_choice, computer_choice_name, user_choice_name)
    

  
play()