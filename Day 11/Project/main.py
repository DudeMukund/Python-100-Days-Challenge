import random
from art_black_jack import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(my_score, computer_score):
    if my_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has blackjack"
    elif my_score == 0:
        return "You win with a blackjack"
    elif my_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif my_score > computer_score:
        return "You win"
    else:
        return "You lose"
play = True

while(play):
    print(logo)
    my_card = []
    computer_card = []
    is_game_continue = True

    for _ in range(2):
        my_card.append(deal_card())
        computer_card.append(deal_card())

    while is_game_continue:
        my_score = calculate_score(my_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {my_card}, current score: {my_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if my_score == 0 or computer_score == 0 or my_score > 21 or computer_score > 21:
            is_game_continue = False
        else:
            choice = input("Type 'hit' to get another card, type 'pass' to pass: ")
            if choice == 'hit':
                my_card.append(deal_card())
            else:
                is_game_continue = False

    
    if my_score <= 21:
        while computer_score != 0 and calculate_score(computer_card) < 16:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)

    print(f"Your final hand: {my_card}, final score: {calculate_score(my_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {calculate_score(computer_card)}")
    print(compare(calculate_score(my_card), calculate_score(computer_card)))

    playing_choice= input("if you want to continue this game Enter 'yes' else 'no' :  ").lower()
    if playing_choice =="no":
        play = False
    else:
        print("\n"*50)

        




    


