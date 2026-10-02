# Day 12: Scope, Namespaces & Number Guessing Game

## What I Learned Today

### Namespace
A **namespace** is a table of **names and the objects they point to**, a lot like a dictionary with key-value pairs.
```python
name = "dude"
```
Here `name` is the key (the name) and `"dude"` is the value (the object). Python keeps these tables for variables, functions, and everything else I name.

### Scope
**Scope** is the part of the code where a name can be **seen and used**.
- **Namespace** = where the name is stored
- **Scope** = where the name is visible

### Local Scope
A variable created **inside a function** is local. I can only use it inside that function. When the function ends, the variable is gone.
```python
def greet():
    message = "Hello"   # local variable
    print(message)      # works

greet()
print(message)          # NameError
```

### Global Scope
A variable created **outside all functions** is global. I can read it anywhere in the file, including inside functions.
```python
label = "Python"        # global variable

def show():
    print(label)        # works, it only reads

show()
```

### Changing a Global Inside a Function
If I assign to a name inside a function, Python creates a **new local variable**. The global one stays the same.
```python
x = 5

def change():
    x = 100             # new local x
    print(x)            # 100

change()
print(x)                # 5, global is unchanged
```
To really change the global, I have to write `global` inside the function:
```python
count = 0

def add():
    global count
    count += 1
```
It works, but it is **not a good practice**. It is better to pass the value in as a parameter and `return` the result.

### Mutable vs Immutable
This is what decides whether a function can change something from the outside.

**Immutable** (int, str, tuple): the object cannot be changed in place. If I change it inside a function, the change stays **only inside that function**. The outside value stays the same.
```python
def change_text(s):
    s = s + " World"    # makes a new string, local only

text = "Hello"
change_text(text)
print(text)             # Hello
```

**Mutable** (list, dict, set): the object can be changed in place. If I add something inside a function, it really changes the original, and I don't need `global`.
```python
def add_item(items):
    items.append(4)

numbers = [1, 2, 3]
add_item(numbers)
print(numbers)          # [1, 2, 3, 4]
```

But if I **replace** the whole list with `items = [99]` inside the function, that only creates a new local variable. Adding or removing items changes the original. Re-assigning does not.

## Main Project: Number Guessing Game
Today's project was a number guessing game where the computer picks a secret number and I have to guess it.

How it works:
- The computer picks a random number between 1 and 100 using `random.randint(1, 100)`.
- The player chooses a difficulty:
  - `easy` gives **10 attempts**
  - `hard` gives **5 attempts**
- After every guess, the game gives a hint based on how far away the guess is: `too high`, `high`, `slightly high`, `very close`, `slightly low`, `low`, and `too low`.
- Each wrong guess uses up one attempt.
- The game stops when the player guesses the number (using `break`) or when the attempts run out.
- I added an ASCII art logo at the start to make it look better.

Things I practiced here:
- `while` loop that depends on the number of attempts left
- `if / elif / else` chain for the hints
- `break` to stop the loop on a correct guess
- Raw string `r"""..."""` for the ASCII art, so backslashes print correctly

## Key Takeaway
A namespace stores names and objects like key-value pairs, and scope decides where those names can be used. Local variables stay inside functions and global variables live outside them. Mutable data types like lists can be changed from inside a function, while immutable ones like strings and numbers cannot. The guessing game showed me how loops, conditions, and `break` work together in one program.