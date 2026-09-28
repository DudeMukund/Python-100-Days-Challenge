import random
def check_guess(guess, target):
    if guess == target:
        return "correct"
    elif guess < target:
        return "low"
    else:
        return "high"

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    
    target_number = random.randint(1, 20)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        result = check_guess(guess, target_number)
        
        if result == "correct":
            print(f"Congratulations! You got it in {attempts} attempts.")
            guessed_correctly = True
        elif result == "low":
            print("Too low, guess again.")
        else:
            print("Too high, guess again.")

play_game()