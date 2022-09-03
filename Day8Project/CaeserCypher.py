###Caeser Cypher###
from art import logo

print(logo)
print("Welcome to Caeser Cypher!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

spec_char = [" ", "!", "@", "#", "$", "%", "^", "&"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(start_text, shift_amount, cipher_direction):
  final_text = ""
  
  for letter in start_text:
    if letter in alphabet:
      index_number = alphabet.index(letter)
      
      if cipher_direction == "encode":
        new_letter = alphabet[(index_number + shift_amount) % len(alphabet)]
      elif cipher_direction == "decode":
        new_letter = alphabet[(index_number - shift_amount) % len(alphabet)]

      final_text += new_letter
    
    else:
      final_text += letter

  print(f"Your {cipher_direction}d text is: {final_text}")
  playAgain()


def playAgain():
  restart = input("Would you like to use this program again?\n'Yes' or 'No'> ").lower()
  if restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
  elif restart == "no":
    print("Goodbye!")
    quit()
  else:
    print("Im not sure what you said, Goodbye!")
    quit()

caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

