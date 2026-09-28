# Day 9: Dictionaries & Silent Auction

## What I Learned Today

### Dictionaries
A dictionary stores data as **key-value pairs**, instead of just a 
list of values. You look things up by key instead of by position 
(index).

Dictionaries are **mutable** — you can add, change, or remove 
key-value pairs after creating one.

**Values** can be literally anything — a string, int, list, another 
dictionary, whatever you need.

**Keys** have a restriction though — they must be an **immutable** 
data type. So `string`, `int`, and `tuple` are all fair game as 
keys, but `list` and `set` are not allowed, since they can change.

### Nesting
Dictionaries can be nested inside each other (a dictionary as a 
value inside another dictionary), and the same goes for lists — you 
can have a list inside a dictionary, or a list inside another list. 
Useful for representing more complex, structured data.

### Dictionary Methods
Got introduced to some built-in functions for working with 
dictionaries — accessing values, checking keys, updating entries, 
etc. Still getting comfortable with all of them, but the basics 
(reading and writing key-value pairs) feel solid now.

## Main Project: Silent Auction

Built a program that runs a silent auction — multiple people can bid 
in secret, and at the end it reveals who bid the highest.

How it works:
- Every bidder's name and bid amount gets stored in a dictionary 
  (`name` as key, `bid` as value).
- After each bid, it asks if there's another bidder — if yes, it 
  clears the screen (using a bunch of newlines) so the next person 
  can't see previous bids.
- Once everyone's done, a `find_highest_bidder()` function loops 
  through the dictionary, keeps track of the highest bid seen so 
  far, and prints out the winner and their winning amount.

This was a good real use-case for dictionaries — mapping each name 
directly to their bid made looking up "who bid what" way simpler 
than trying to juggle two separate lists.

## Key Takeaway
Dictionaries click a lot more once you actually use them for 
something practical. Being able to store related data together as 
key-value pairs (instead of matching up indexes across two lists) 
made the silent auction project way cleaner to write than it would've 
been otherwise.