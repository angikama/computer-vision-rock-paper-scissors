import random

choices = ['Rock', 'Paper', 'Scissors ']

# randomly choses an action for the computer      
def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice
    

# gets input from the user using intergers
def get_user_choice():
    user_choice = input("Do you choose Rock, Paper or Scissors?: ")
    return user_choice


# decides who wins
def get_winner():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print()
    print(f"You chose {user_choice} and the Computer chose {computer_choice}")

    if computer_choice == user_choice:
            print ("You Draw!")
    elif (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Scissors' and user_choice == 'Rock') or (computer_choice == 'Paper' and user_choice == 'Scissors'):
            print("You win!")
    elif (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
            print("The computer wins!")
    
    
def play_again():
    get_winner()
       
# allows the whole game to be played
def play():
    get_winner()
    rounds = 3
    while rounds < 3:
        play_again()
        rounds+=1

play()
