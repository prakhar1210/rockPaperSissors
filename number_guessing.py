# import random

# def number_guessing():
#     targetNumber = random.uniform(1, 100)
#     attempts = 5

#     print("Welcome to the number guessing game !!")
#     print("I am thinking of a number in a range of 1 - 100. Can you guess it???")
#     print(f"You have {attempts} to guess the number correctly. Lets start:")

#     for attempt in range(1, attempts+1):
#         while True:
#             # make the guess
#             guess = int(input(f'Attempt {attempt}/{attempts}: Enter your guess: '))

#             # if the guess is right
#             if guess == targetNumber:
#                 print(f"🎉 Congratulations! You guessed the number {targetNumber} correctly!")
#                 break
#             elif guess < targetNumber:
#                 print("Too low! Try again.")
#             else:
#                 print("Too high! Try again.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")
        
#         # If it's the last attempt and the number is not guessed
#         if attempt == attempts:
#             print(f"😔 Sorry, you've used all your attempts. The correct number was {targetNumber}.")
#         play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
#         if play_again != "yes":
#             print("Thank you for playing! Goodbye!")
#             break

# number_guessing()


import random

def number_guessing_game():
    while True:
        # Generate a random number between 1 and 100
        target_number = random.randint(1, 100)
        attempts = 5  # Maximum number of attempts allowed
        
        print("\nWelcome to the Number Guessing Game!!")
        print("I am thinking of a number in the range of 1 - 100. Can you guess it???")
        print(f"You have {attempts} chances to guess the number correctly. Let's start!")
        
        for attempt in range(1, attempts + 1):
            try:
                # Take user input
                guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
                
                # Check the guess
                if guess == target_number:
                    print(f"🎉 Congratulations! You guessed the number {target_number} correctly!")
                    break
                elif guess < target_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            
            # If it's the last attempt and the number is not guessed
            if attempt == attempts:
                print(f"😔 Sorry, you've used all your attempts. The correct number was {target_number}.")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

# Run the game
number_guessing_game()
