import random

class RPS():

# randomly choses an action for the computer      
    def get_computer_choice(computer_choice):
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            computer_choice = "Rock"
        elif computer_choice == 2:
            computer_choice = "Paper"
        else:
            computer_choice == 3
            computer_choice = "Scissors"
        return computer_choice
        

# gets input from the user using intergers
    def get_user_choice(user_choice):
        user_choice = input("Do you choose (Rock[1], Paper[2] or Scissors[3]?: ")
        user_choice = int(user_choice)

        if user_choice == 1:
            user_choice = "Rock"
        elif user_choice == 2:
            user_choice = "Paper"
        else:
            user_choice == 3
            user_choice = "Scissors"
        return user_choice


# decides who wins
    def get_winner(self,computer_choice, user_choice):
        print()
        print(f"You chose {user_choice} and the Computer chose {computer_choice}")
        print()
        

        while True:
            if computer_choice == user_choice:
                print ("You Draw!")
            
            elif computer_choice == 1:
                if user_choice == 2:
                    print("You win!")     
                else:
                    print("The computer wins!")
                           
            elif computer_choice == 2:
                if user_choice == 1:
                    print("The computer wins")   
                else:
                    print("You win!")
                
            elif computer_choice == 3:
                if user_choice == 1:
                    print("You win!")
                    user_wins+=1
                else:
                    print("The computer wins!")
                    
    
            play_again = input("Do you want to play again? (y/n) : ").lower()
            if play_again == "n":
                break
            else:
                play()

    
             
# allows the whole game to be played
def play():
    game = RPS()
    computer_choice = game.get_computer_choice()
    user_choice = game.get_user_choice()
    game.get_winner(computer_choice, user_choice)


  
play()