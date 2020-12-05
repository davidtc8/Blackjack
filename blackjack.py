import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck"""
    random_card = random.choice(cards)
    cards.remove(random_card)
    return random_card

#Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for card in range(2):
    user_cards.append(deal_card())


for card in range(2):
    computer_cards.append(deal_card())

#function called calculate_score() that takes a List of cards as input and returns the score.

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

    #Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []

    for card in range(2):
        user_cards.append(deal_card())

    for card in range(2):
        computer_cards.append(deal_card())

    #Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.

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

#Restart game
while input("Would you like to play another game? Type 'yes' or 'no': ") == 'yes':
    restart()
