import cv2
from keras.models import load_model
import numpy as np
import time
import random

# Global Variables
choices = ['Rock', 'Paper', 'Scissors ']

def countdown (t):
    '''
    Countdown timer

    Parameters:
    -----------
        t

    '''
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(2)
        t -= 1
    print("You chose...")


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

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.start_time = time.time()
        
        while self.start_time > time.time(): 
            self.ret,frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            self.user_choice = np.argmac(prediction[0])
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            return self.user_choice
         # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    
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
            self.computer_choice = random.choice(choices)
            return self.computer_choice
    
    def get_user_choice(self, camera = True, duration = 3):
        if camera:
            self.user_choice = self.get_prediction(duration)
            return self.user_choice


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
                countdown(10)
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

