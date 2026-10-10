`# Day 14: Higher Lower Game

## What I Learned Today

No new theory today. Today was project work: I built the **Higher Lower
game** (guess which celebrity has more Instagram followers), and it
pulled together what I learned from Day 1 to Day 14: `while` loops,
`if`/`elif`/`else`, functions, f-strings, imports from other files, and
the `random` module.

### How the project works
- Two random celebrities are picked from `game_data`, and the player
  guesses who has more followers by typing `A` or `B`.
- `.upper()` on the input means lowercase `a` or `b` also works.
- If A and B are the same person, the game asks the player to run it
  again instead of crashing.
- A right answer adds 1 to the score. If B was the right answer, B
  becomes the new A for the next round.
- A wrong answer prints "Game over" with the final score and ends the
  `while game_continue:` loop.
- `clear()` uses `os.system` (`cls` on Windows, `clear` on Linux/Mac),
  so the previous round disappears from the terminal before the next
  one is printed.
- The logo and VS art are imported from `art.py`, and the celebrity
  data from `game_data.py`.

## Honest Reflection

This one was hard for me to build, but I made it in my own way and did
not copy it from anywhere. The logic works: the score, the winner
carrying over as A, and the game-over condition all behave correctly.

My regret is that I did not use functions. I only wrote one small
function (`clear()`), and the first round and the `while` loop repeat
almost the same code. Functions are important, and this project showed
me where I should have used them.

## Key Takeaway
Writing a working program on my own is a real step forward, and getting
it working matters more than making it short. The next improvement is
making it clean: moving the repeated code into functions (for example
one to format a celebrity, one to compare followers, and one to run a
round) so each change only has to be made in one place. I will try that
on the next project.`