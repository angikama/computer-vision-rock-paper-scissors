# Computer Vision - Rock, Paper, Scissors

The computer model is trained using pictures showing the rock, paper, scissors gestures. The model is able to detect what gesture is being shown to the camera. 

- A new conda environment (my_env) was created, and the following libraries were installed using pip
  - tensorflow
  - ipykernel
  - opencv-python

The code within manual_rps.py, codes for a simple Rock, Paper, Scissors game. The computer choses a random action from the list of actions, and the user inputs their choice. The choices are compared against the conditions listed in the function get_winner to determine a winner. The user is asked if they want to play again at the end of the game.

Through integrating the manual script and the computer vision model, the user can play 'Rock Paper Scissors' using the webcam to physically select an action.

