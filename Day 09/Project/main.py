Bidders_names = {}
is_biding_continue = True

from art import logo
print(logo)

def find_highest_bidder(Bidders_dictionary):
    '''Here we are finding who is highest bidder and how much it bids'''
    winner =""
    max_bids = 0
    for i in Bidders_names:
        if Bidders_names[i] > max_bids:
            max_bids = Bidders_names[i]
            winner = i
    print(f"The winner is {winner} with a bid of ${max_bids}")


while is_biding_continue :
   
    name = input("Enetr your name? ")
    bid = int(input("what's your bid: $"))
    
    Bidders_names[name] = bid
    
    should_continue =input("Are there any other bidder? type 'yes' or 'no'.\n").lower()

    if should_continue == 'no':
        find_highest_bidder(Bidders_names)
        is_biding_continue = False
    else:
        print("\n" * 20)
    




