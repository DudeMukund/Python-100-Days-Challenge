import os 
import random
from art import logo, vs
from game_data import data

score = 0
celb_A = random.choice(data)
celb_B = random.choice(data)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if celb_A != celb_B:
    print(logo)
    print(f"Comapre A: {celb_A["name"]}, a {celb_A["description"]}, {celb_A["country"]}")
    print(vs)
    print(f"Against B: {celb_B["name"]}, a {celb_B["description"]}, {celb_B["country"]}")

    choice = input("Who has more followers? Type 'A' or 'B':  ").upper()

    if choice == 'A' and celb_A["follower_count"] > celb_B["follower_count"]:
        score += 1
        game_continue = True
    elif choice == 'B'and celb_B["follower_count"] > celb_A["follower_count"]:
        score += 1
        game_continue = True
        celb_A = celb_B
    else:
        print(f"Game over! you are wrong. Final score is {score}")
        game_continue = False
else:
    print("run one more time")
    game_continue = False

while game_continue:
    
    clear()
    print(logo)
    celb_N = random.choice(data)

    if celb_A != celb_N:
        print(f"you are right! current score: {score}.")

        print(f"Comapre A: {celb_A["name"]}, a {celb_A["description"]}, {celb_A["country"]}")

        print(vs)

        print(f"Against B: {celb_N["name"]}, a {celb_N["description"]}, {celb_N["country"]}")

        choice = input("Who has more followers? Type 'A' or 'B':  ").upper()

    

        if choice == 'A' and celb_A["follower_count"] > celb_N["follower_count"]:
            score += 1
            game_continue = True
        elif choice == 'B'and celb_N["follower_count"] > celb_A["follower_count"]:
            score += 1
            game_continue = True
            celb_A = celb_N
        else:
            print(f"Game over! you are wrong. Final score is {score}")
            game_continue = False
            



