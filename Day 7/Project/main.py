import random
import hangman_art
from  hangman_words import word_list

print(hangman_art.logo)

word = random.choice(word_list)
lives = 6
display = ["_"] * len(word)

while lives > 0:
    print("word to guess :", display)
    print("Lives remaining:", "❤️ " * lives)
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print(hangman_art.stages[lives])
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])

    if "_" not in display:
        print("You win! The word was:", word)
        break

    if lives == 0:
        print("You lose! The word was:", word)