############### Blackjack Project #####################
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck"""
    random_card = random.choice(cards)
    cards.remove(random_card)
    return random_card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for card in range(2):
    user_cards.append(deal_card())


for card in range(2):
    computer_cards.append(deal_card())

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

total_user = 0
total_computer = 0

def calculate_score(total_user, total_computer):
    for card in user_cards:
        total_user += card
    for card in computer_cards:
        total_computer += card
    if total_computer == 21:
        print('The computer has won!')
    elif total_user == 21:
        print('you have won!')
    return f"The user has: {user_cards}, user score: {total_user}\nComputer has: {computer_cards[0]} and another random card, Computer score: {computer_cards[0]}"

print(calculate_score(total_user, total_computer))

def final_score(total_user, total_computer):
    for card in user_cards:
        total_user += card
    for card in computer_cards:
        total_computer += card
    return f"The user has: {total_user}\nComputer has: {total_computer}"

if sum(user_cards) < 21 and sum(computer_cards) < 21:
    decision = input("Would you like another card? (type yes or no): ").lower()
    if decision == 'yes':
        for card in user_cards:
            card_given = deal_card()
            user_cards.append(card_given)
            print(f"You received a {card_given}")
            break
        ace = 11
        blackjack = 21
        if ace in user_cards and total_user > blackjack:
            user_cards.remove(ace)
            user_cards.append(1)
            total_user = 0
            for card in user_cards:
                total_user += card
            print(f"You converted the {ace} to 1, and the total you have is: {total_user}")
elif sum(computer_cards) == 21:
    decision = 0
    print("Game Over!")
else:
    decision = 0
    print("Game Over!")

if sum(computer_cards) <= 17 and decision != 0:
    for card in computer_cards:
        next_computer_card = deal_card()
        print(f"The computer decided to take another card ({next_computer_card})")
        computer_cards.append(next_computer_card)
        break

print(final_score(total_user, total_computer))

def compare():
    if sum(computer_cards) > 21:
        print(f"The computer loses because he has {computer_cards}, computer score: {sum(computer_cards)}")
        if sum(user_cards) > 21:
            print(f"Both you and the computer lost, User Score: {user_cards}")
        else:
            print(f"you have won! User Score: {user_cards}")
    elif sum(user_cards) > 21:
        print(f"You lost because you have {user_cards}, user score: {sum(user_cards)}")
        if sum(computer_cards) > 21:
            print(f"Both you and the computer lost, computer score: {computer_cards}")
        else:
            print(f"The computer has won! Computer score: {computer_cards}")
    elif sum(user_cards) == sum(computer_cards):
        print("It's a draw")
    elif sum(computer_cards) == 21:
        print(f"The computer has won! Computer score: {computer_cards}")
    elif sum(user_cards) == 21:
        print(f"you have won! User Score: {sum(user_cards)}")
    elif sum(user_cards) > sum(computer_cards) and sum(user_cards) < 21:
        print(f"you have won! User Score: {user_cards}")
    elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) < 21:
        print(f"The computer has won! Computer score: {computer_cards}")

if decision != 0:
    compare()

def restart():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card():
        """Returns a random card from the deck"""
        random_card = random.choice(cards)
        cards.remove(random_card)
        return random_card

    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []

    for card in range(2):
        user_cards.append(deal_card())

    for card in range(2):
        computer_cards.append(deal_card())

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.
    #Look up the sum() function to help you do this.

    total_user = 0
    total_computer = 0

    def calculate_score(total_user, total_computer):
        for card in user_cards:
            total_user += card
        for card in computer_cards:
            total_computer += card
        if total_computer == 21:
            print('The computer has won!')
        elif total_user == 21:
            print('you have won!')
        return f"The user has: {user_cards}, user score: {total_user}\nComputer has: {computer_cards[0]} and another random card, Computer score: {computer_cards[0]}"

    print(calculate_score(total_user, total_computer))

    def final_score(total_user, total_computer):
        for card in user_cards:
            total_user += card
        for card in computer_cards:
            total_computer += card
        return f"The user has: {total_user}\nComputer has: {total_computer}"

    if sum(user_cards) < 21 and sum(computer_cards) < 21:
        decision = input("Would you like another card? (type yes or no): ").lower()
        if decision == 'yes':
            for card in user_cards:
                card_given = deal_card()
                user_cards.append(card_given)
                print(f"You received a {card_given}")
                break
            ace = 11
            blackjack = 21
            if ace in user_cards and total_user > blackjack:
                user_cards.remove(ace)
                user_cards.append(1)
                total_user = 0
                for card in user_cards:
                    total_user += card
                print(f"You converted the {ace} to 1, and the total you have is: {total_user}")
    elif sum(computer_cards) == 21:
        decision = 0
        print("Game Over!")
    else:
        decision = 0
        print("Game Over!")

    if sum(computer_cards) <= 17 and decision != 0:
        for card in computer_cards:
            next_computer_card = deal_card()
            print(f"The computer decided to take another card ({next_computer_card})")
            computer_cards.append(next_computer_card)
            break

    print(final_score(total_user, total_computer))

    def compare():
        if sum(computer_cards) > 21:
            print(f"The computer loses because he has {computer_cards}, computer score: {sum(computer_cards)}")
            if sum(user_cards) > 21:
                print(f"Both you and the computer lost, User Score: {user_cards}")
            else:
                print(f"you have won! User Score: {user_cards}")
        elif sum(user_cards) > 21:
            print(f"You lost because you have {user_cards}, user score: {sum(user_cards)}")
            if sum(computer_cards) > 21:
                print(f"Both you and the computer lost, computer score: {computer_cards}")
            else:
                print(f"The computer has won! Computer score: {computer_cards}")
        elif sum(user_cards) == sum(computer_cards):
            print("It's a draw")
        elif sum(computer_cards) == 21:
            print(f"The computer has won! Computer score: {computer_cards}")
        elif sum(user_cards) == 21:
            print(f"you have won! User Score: {sum(user_cards)}")
        elif sum(user_cards) > sum(computer_cards) and sum(user_cards) < 21:
            print(f"you have won! User Score: {user_cards}")
        elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) < 21:
            print(f"The computer has won! Computer score: {computer_cards}")

    if decision != 0:
        compare()

while input("Would you like to play another game? Type 'yes' or 'no': ") == 'yes':
    restart()
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
