############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


########## This is a project that I finished without hints ###########
########## There are many errors and the code is real messy ##########



import random
from art import logo




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = [random.choice(cards), random.choice(cards)]
user_hand = [random.choice(cards), random.choice(cards)]
dealer_total = sum(dealer_hand)
user_total = sum(user_hand)



def check_total():
    print(f"\n\nDealers first card is {dealer_hand[0]}")
    print(f"Users hand is {user_hand}, Total is {sum(user_hand)}")

def more_cards():
    ask_for_card = True
    while ask_for_card:
        new_card = input ("Would you like another card? Y/N: ").lower()
        if new_card == "y":
            user_hand.append(random.choice(cards))
            check_total()
              
            if sum(user_hand) > 21 and 11 in user_hand:
                user_hand.remove(11)
                user_hand.append(1)
                check_total()
            elif sum(user_hand) > 21:
                print("You went over 21, you lose!")
                print(f"Dealers cards were {dealer_hand}, with a total of {sum(dealer_hand)}")
                
            elif sum(dealer_hand) > 21:
                print(f"Dealers cards were {dealer_hand}, with a total of {sum(dealer_hand)}")
                print("You Win!")
                
        else:
            ask_for_card = False

check_total()

if sum(dealer_hand) < 17:
    dealer_hand.append(random.choice(cards))
    if sum(dealer_hand) > 21 and 11 in dealer_hand:
        dealer_hand.remove(11)
        dealer_hand.append(1)

more_cards()
check_total()

if sum(dealer_hand) > sum(user_hand) and sum(dealer_hand) <= 21:
    print("Dealer Wins!")
    print(f"Dealers cards were {dealer_hand}, with a total of {sum(dealer_hand)}")
elif sum(user_hand) > sum(dealer_hand) and sum(dealer_hand) <= 21:
    print(f"Dealers cards were {dealer_hand}, with a total of {sum(dealer_hand)}")
    print("User Wins!")
elif sum(user_hand) == sum(dealer_hand):
    print("Draw!")
    print(f"Dealers cards were {dealer_hand}, with a total of {sum(dealer_hand)}")

