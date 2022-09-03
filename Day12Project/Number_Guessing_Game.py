### Number Guessing Game ###
# Easy and Hard Mode
# Easy mode has 10 guesses
# Hard mode has 5 guesses
# 1 - 100
# Tell if number is higher or lower than guess
# Tell how many attempts you have left
import random

EASY_LIVES = 10
HARD_LIVES = 5

print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")

def difficulty_choice():
    difficulty = input("Would you like to play on 'Easy' or 'Hard'?: ").lower()
    if difficulty == "easy":
        return EASY_LIVES
    elif difficulty == "hard":
        return HARD_LIVES


def lose_game(lives, guess):
    if lives == 0:
            print(f"You're Out of lives! You lose!\n The correct number was {guess}")
            exit()
    else:
        return
    

def game():
    random_number = random.randint(1, 100)
    number_guessed = False
    lives = difficulty_choice()
    print(f"You have {lives} lives")
    
    while number_guessed == False:
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print(f"Thats correct, the number was {random_number}! You win!")
            number_guessed = True
        elif guess > random_number:
            print("\nYour guess was too high!")
            lives -= 1
            lose_game(lives, guess)
            print(f"You have {lives} lives left.")
        elif guess < random_number:
            print("\nYour guess was too low!")
            lives -= 1
            lose_game(lives, guess)
            print(f"You have {lives} lives left.")
        else:
            print("That must have been an invalid input.")

game()

