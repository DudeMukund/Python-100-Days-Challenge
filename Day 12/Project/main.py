import random

logo = r"""
   ___                       _   _                __                 _               
  / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
"""
print(logo)
target = random.randint(1,100)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Choose a difficulty. Type 'easy' or 'hard': ")
game_level = input().lower()
if game_level == 'easy':
    attempt = 10
else:
    attempt = 5


while attempt >0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess:  "))
    if guess == target:
        print("congrats!")
        print(f"You got it! The answer was {guess}")
        break
    elif guess  >=target + 20:
        print("too high!.")
        attempt -=1
    elif guess >= target + 10:
        print("high!.")
        attempt -=1
    elif guess >= target + 5:
        print("slightly high!.")
        attempt -=1
    elif guess <=target - 20:
        print("too low!.")
        attempt -=1
    elif guess <= target - 10:
        print("low!.")
        attempt -=1
    elif guess <= target - 5:
        print("slightly low!.")
        attempt -=1
    else:
        print("very close!")
        attempt -=1

    if attempt == 0:
        print("You've run out of guesses. Refresh the page to run again.")

        






