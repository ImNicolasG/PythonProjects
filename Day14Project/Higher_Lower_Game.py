### Higher/Lower Game ###
import random
from art import logo, vs
from data import data
import os

print(logo)

score = 0
wrong_guess = False

first_choice = random.choice(data) # gets set of info
first_choice_num = first_choice['follower_count'] # gets follower count

while wrong_guess == False: # Loops the game 
    second_choice = random.choice(data) # gets second set of info
    second_choice_num = second_choice['follower_count'] # second follower count
    
    if first_choice_num == second_choice_num: # if second follower count == first follower count
        second_choice = random.choice(data) # get new set of data
        second_choice_num = second_choice['follower_count'] # get follower count from new set

    os.system("cls")
    print(logo) # clears screen, prints logo, and gives score
    print(f"Your score is {score}")

    ## Input which you think is higher
    higher_choice = input(f"""
    Which is higher?
    'A': {first_choice['name']} who is a {first_choice['description']} from {first_choice['country']}
    {vs}
    'B': {second_choice['name']} who is a {second_choice['description']} from {second_choice['country']}?: """).lower()
    
    if higher_choice == "a" and first_choice_num > second_choice_num: # If your choice is A and first choice is greater than second choice, keep going
        print("\n\nThats correct")
        score += 1
        first_choice = second_choice
        first_choice_num = second_choice_num
    elif higher_choice == "b" and second_choice_num > first_choice_num: # If your choice is B and second choice is greater than first choice, keep going
        print("\n\nThats correct")
        score += 1
        first_choice = second_choice
        first_choice_num = second_choice_num
    else:
        print("That was incorrect, You lose.")
        wrong_guess = True


print(f"Your final score was {score}, Thanks for playing!")
