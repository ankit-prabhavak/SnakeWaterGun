#Project: snake , water and gun.

import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
def speak(text):
    engine.say(text)
    engine.runAndWait()



# Function to explain the game rules
def explain_game():
    print("Welcome to the game: Snake, Water, Gun!")
    speak("Welcome to the game: Snake, Water, Gun!")
    print("Here are the rules:")
    speak("Here are the rules:")
    print("1. Snake beats Water.")
    speak("1. Snake beats Water.")
    print("2. Water beats Gun.")
    speak("2. Water beats Gun.")
    print("3. Gun beats Snake.")
    speak("3. Gun beats Snake.")
    print("To play, simply choose one of the options: Snake, Water, or Gun.")
    speak("To play, simply choose one of the options: Snake, Water, or Gun.")
    print("Let's begin!")
    speak("Let's begin!")

# Function to get the player's choice
def player_choice():
    print("\nChoose one: Snake, Water, or Gun")
    speak("Snake, Water, or Gun")
    choice = input("Enter your choice: ").lower()
    while choice not in ['snake', 'water', 'gun']:
        print("Invalid choice. Please choose again: Snake, Water, or Gun.")
        speak("Invalid choice. Please choose again: Snake, Water, or Gun.")
        choice = input("Enter your choice: ").lower()
    return choice

# Function to determine the computer's choice
def computer_choice():
    return random.choice(['snake', 'water', 'gun'])

# Function to decide the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'snake' and computer == 'water') or (player == 'water' and computer == 'gun') or (player == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

# Start the game
explain_game()

# Game loop
while True:
    # Get choices
    player = player_choice()
    computer = computer_choice()
    
    print(f"Your choice: {player.capitalize()}")
    speak(f"Your choice: {player.capitalize()}")
    print(f"Computer's choice: {computer.capitalize()}")
    speak(f"Computer's choice: {computer.capitalize()}")
    
    # Determine the winner
    result = determine_winner(player, computer)
    print(result)
    speak(result)
    
    # Ask if the player wants to play again
    speak("Do you want to play again? (yes/no)")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        speak("Thanks for playing!")
        break
