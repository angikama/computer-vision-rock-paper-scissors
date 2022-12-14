# Rock, Paper, Scissors Game
import random

choices = ['Rock', 'Paper', 'Scissors ']

class RPS():
    '''
    This class represents the Rock, Paper, Scissors game

    Attributes:
    -----------
        None

    Methods:
    ----------
        __init__ (self)

    '''

    def __init__(self):
        '''
        Class constructor for the RPS object

        '''
        self.user_wins = 0
        self.computer_wins = 0 

    def get_computer_choice(self):
        '''
        Randomly selects a choice for the computer

        Parameters:
        -----------
            None
        
        Returns:
        -----------
            computer_choice
        '''
        computer_choice = random.choice(choices)
        return computer_choice
    
    def get_user_choice(self):
        '''
        Allows user to input a choice

        Parameters:
        -----------
            None
        
        Returns:
        ----------
            user_choice
        '''
        user_choice  = input("Do you choose Rock, Paper or Scissors?: ")
        return user_choice
    
    def get_winner(self, computer_choice, user_choice):
        '''
        Determines which player wins the game

        Parameters:
        ------------
            computer_choice - randomly generated choice for computer
            user_choice - input by user

        Returns:
        -----------
            None

        '''
        print('')
        print(f"You chose {user_choice} and the Computer chose {computer_choice}")
        print('')
        if computer_choice == user_choice:
                print ("You Draw!")
        elif (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Scissors' and user_choice  == 'Rock') or (computer_choice == 'Paper' and user_choice  == 'Scissors'):
                print("You win!")
                self.user_wins +=1
        elif (computer_choice == 'Rock' and user_choice  == 'Scissors') or (computer_choice == 'Paper' and user_choice  == 'Rock') or (computer_choice == 'Scissors' and user_choice  == 'Paper'):
                print("The computer wins!")
                self.computer_wins+=1
        print(f"Your score is {self.user_wins} and the computer's score is {self.computer_wins}")
        print('')
    

def play():
    '''
    Allows the whole game to be played

    Parameters:
    ------------
        None

    Returns:
    -----------
        None
        
    '''
    game = RPS()
    while True:
        if game.user_wins < 3 and game.computer_wins < 3:
            computer_choice = game.get_computer_choice()
            user_choice = game.get_user_choice()
            game.get_winner(computer_choice, user_choice)
        elif game.user_wins >= 3:
            print("Congratulations! You won!")
            break
        else:
            game.computer_wins >= 3
            print("Oh no! The computer beat you")
            break

play()
