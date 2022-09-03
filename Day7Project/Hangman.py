import random
from hangman_art import stages, logo
from hangman_words import word_list
#Learning How to create Hangman

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
lives = 6
inputs = []

# print(f"Chosen word is {chosen_word}")



for _ in chosen_word:
    display += "_"


print(logo)
print(stages[lives])
print(display)


end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  print("\n\n\n")
  
  if guess in display:
    print(f"Youve already guessed {guess}")
  
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      print(f"You guessed '{guess}'!")
      display[position] = guess


  if guess not in display:
    lives -= 1
    print(f"\n\n\nYou guessed '{guess}', thats not in the word")
    if lives == 0:
      print(f"The word was {chosen_word}")
      print("You lose!")
      end_of_game = True
  
  
  print(stages[lives])
  print(display)


  if "_" not in display:
    end_of_game = True
    print(f"The word was {chosen_word}!")
    print("You Win!!")
    
    













