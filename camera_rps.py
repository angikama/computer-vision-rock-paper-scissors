import cv2
from keras.models import load_model
import numpy as np
import time
import random

# Global Variables
choices = ['Rock', 'Paper', 'Scissors ']

#Countdown Timer - 30 seconds time.sleep?
def countdown (t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    
    print("You chose...")

countdown(30)

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


# randomly choses an action for the computer      
def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

    
# gets input from the user
def get_user_choice():
    user_choice = input("Do you choose Rock, Paper or Scissors?: ")
    return user_choice


# decides who wins
def get_winner(computer_choice, user_choice):
    print(f"You chose {user_choice} and the Computer chose {computer_choice}")
    if computer_choice == user_choice:
            print ("You Draw!")
    elif (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Scissors' and user_choice == 'Rock') or (computer_choice == 'Paper' and user_choice == 'Scissors'):
            print("You win!")
    elif (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
            print("The computer wins!")

# allows the game to be played
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(user_choice, computer_choice)
        
play()
