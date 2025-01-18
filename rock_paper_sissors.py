import random

choices = ['rock', 'paper', 'scissors']

# Function to get input from the user
def input_from_user(choices):
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    if user_choice in choices:
        print(f"Your choice is: {user_choice}")
        return user_choice
    else:
        print("Invalid choice! Please select from the given options: rock, paper, or scissors.")
        return None

# Function to generate the computer's choice
def computer_choice(choices):
    computer = random.choice(choices)
    print(f"The computer's choice is: {computer}")
    return computer

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "Hey, it's a tie!!!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "🎉 Congratulations!! You Win!"
    else:
        return "Computer Wins!!! Better luck next time."

# Main game function
def game_function():
    print("Welcome to Rock, Paper, Scissors game !!!")

    while True:
        # Get user input
        user_choice = input_from_user(choices)
        if not user_choice:  # If the user input is invalid, restart the loop
            continue

        # Get computer choice
        computer_choice_result = computer_choice(choices)

        # Determine winner
        result = determine_winner(user_choice, computer_choice_result)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Call the game function
game_function()
