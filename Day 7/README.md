# Day 7: Hangman Game (while, for, if, import)

## What I Learned Today

### Recap + New Concepts Used

Built on functions and while loops from Day 6, and pulled in a few 
new pieces to build a working Hangman game.

**`import`**
Used to bring in code from another file/

**`if` / `else` inside a loop**
Used to branch behavior each round — checking whether the guessed 
letter is actually in the word, and reacting differently depending 
on the result (reveal letter vs. lose a life).

**Building a string letter-by-letter**
Learned that strings are **immutable** — you can't do 
`display[0] = "m"` directly. Instead, I rebuild the display string 
fresh every round using `+=`, checking each letter of the word 
against a list of letters guessed so far.

**Lists for tracking state**
Used a plain list (`guessed_letters = []`) to remember every letter 
guessed across iterations, since the while loop resets local 
variables each time but the list persists outside the loop.

## Project
### Hangman
A word-guessing game where the player has a limited number of lives 
(6) and guesses one letter at a time. Correct guesses reveal that 
letter's position(s) in the word; wrong guesses cost a life and show 
the next stage of hangman ASCII art. The loop keeps running via 
`while lives > 0`, checking a win condition (`"_" not in display`) 
and a lose condition (`lives == 0`) each round.

## Key Takeaway
`for` loops made character-by-character comparisons much cleaner 
than manually indexing with `while`. Also finally understood *why* 
strings are immutable in practice — trying to "edit" one directly 
threw errors, which pushed me to rebuild the display string from 
scratch each round instead.