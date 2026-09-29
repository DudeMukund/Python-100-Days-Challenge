# Day 11: Blackjack Project

## What I Learned Today

No new theory today — today was pure project work. Built a **Blackjack 
game**, and it ended up pulling together pretty much everything from 
Day 1 to Day 10: `while` loops, `for` loops, functions, `if`/`else`, 
and the `random` module all showed up in this one project.

### How the project works
- `deal_card()` picks a random card value from a list (face cards as 
  10, Ace as 11 by default).
- `calculate_score()` adds up a hand's cards, and handles the tricky 
  part — if an Ace is pushing the total over 21, it gets converted 
  from 11 down to 1.
- The player's turn runs in a `while` loop — hit or pass, repeated 
  until they bust, hit blackjack, or choose to stop.
- Once the player's turn ends, the dealer plays automatically in its 
  own loop, drawing cards until its score hits 16 or higher.
- A `compare()` function checks both final scores and decides win, 
  lose, or draw.
- Wrapped the whole thing in an outer `while play:` loop so the game 
  can be replayed without restarting the script.

## Honest Reflection

Today wasn't a great day, and I want to be honest about it instead of 
skipping over it. This project came from the course I'm doing with 
Angela Yu — she demoed how the project works but didn't share the 
code — the idea was to build it myself first, then compare against 
her solution. Today, I'd say I only contributed about **10-20%** on 
my own, and the rest came from following Angela's solution.

I do understand the concepts involved — the loops, the functions, the 
logic for handling the Ace, the turn structure — none of that felt 
foreign. But actually *producing* the code on my own, structuring the 
game flow, catching my own bugs (like forgetting to set a loop flag to 
`False`, or calling a function without `()`) — that part I struggled 
with a lot today.

## Key Takeaway
Understanding a concept and being able to independently build something 
with it are two different skills, and today made that gap pretty clear. 
That's fine — it's part of the process, and it happens to everyone. 
The plan going forward is to keep leaning on smaller projects to close 
that gap between "I get it when I see it" and "I can write it myself."