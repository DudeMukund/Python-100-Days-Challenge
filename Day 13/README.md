 # Day 13: Debugging

## What is Debugging?
**Debugging** is the process of finding, understanding, and fixing mistakes (called **bugs**) in your code. A bug is anything that makes your program crash, give a wrong result, or behave differently from what you expected. Debugging is not about guessing. It is about investigating the problem step by step until you find the exact cause.

## What I Learned Today

### 1. Don't Jump Straight Into the Code
When something breaks, don't start changing random lines. Slow down and go **step by step**. Understand what the code is supposed to do, then find where it stops doing that.

### 2. Become the Computer
Before running the code, read it line by line and **run it in your head**, exactly like the computer would:
- What is the value of each variable after every line?
- Which `if` condition becomes true? How many times does the loop run?
- Where does the output stop matching what I expected?

Many bugs are found at this stage, without even running the program.

### 3. Use `try` and `except`
`try` and `except` let you handle errors without the whole program crashing.
- Python first **tries** to run the code inside `try`.
- If it works, the `except` block is skipped.
- If it fails, Python jumps to the `except` block and runs that instead, so I can show a message about what went wrong.

**Example 1: Dividing by zero**
```python
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: You can't divide a number by zero!")
```

**Example 2: Wrong user input**
```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("Error: Please enter a number, not text!")
```

**Example 3: File that doesn't exist**
```python
try:
    with open("notes.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: That file doesn't exist.")
```

**Example 4: Using `else` and `finally`**
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That was not a valid number.")
else:
    print(f"Great, you entered {number}")   # runs only if no error happened
finally:
    print("Done!")                          # runs every time, error or not
```

### 4. Use `print()` to Check Values
Whatever problem I'm facing, **print the values on each important line** and ask: *"Is this value what I expected?"*
```python
def add(a, b):
    print(f"a = {a}, b = {b}")      # check inputs
    total = a + b
    print(f"total = {total}")       # check result
    return total
```
The first place where a printed value looks wrong is usually very close to the bug.

### 5. Comment Out Code to Find the Bug
Imagine I have **15 lines of code** and don't know which one is wrong:
1. Comment out line 15 and run it. Does it work?
2. Comment out line 14 as well and run it again.
3. Keep going upward, one line at a time.
4. Say I comment out line 13 and the error **disappears**. That means the problem is in line 13.

This way I narrow the problem down from the whole program to a single line.

### 6. Use a Debugger
A **debugger** is a tool that runs my code **step by step** and shows me what is happening at each step: which line is running, and what every variable currently holds. I can pause the program at any line (a **breakpoint**) and look inside. VS Code has one built in.

### 7. Take a Break
If I'm stuck, **step away**: go for a walk, or come back in the evening or the next day. Very often I return with fresh eyes and spot the bug almost immediately. It really works.

### 8. Ask for Help
- **Stack Overflow**: someone has probably faced the same error already.
- **Friends** who are also learning programming.
- **Developers** who can look at the code with experience.

### 9. Ask AI, But the Right Way
AI can help, but the way I use it matters:
- Don't paste the code and ask for the final answer.
- Ask **"What is the bug?"** or **"Where might the problem be?"** and then fix it myself.
- Asking for the full solution should be the **last step**, not the first.
- In the early phase of learning, try to avoid AI as much as possible, because struggling with the bug is where the learning happens.

### 10. Bugs Are Normal
Creating bugs is a normal part of learning to code. I'm a beginner, so of course I make bugs. Even professional developers create bugs, and bigger ones too. That's how they became professionals: by finding and fixing them. Debugging is part of the journey to becoming a Python developer.

## Debugging Checklist
1. Read the error message carefully
2. Go step by step, don't panic
3. Become the computer and trace the code in my head
4. `print()` the values
5. Comment out code to isolate the bug
6. Use `try` / `except` where errors are expected
7. Use the debugger
8. Take a break
9. Ask other people, then AI (for hints first)

## Project
No project today. Day 13 was all about learning *how to debug*, and debugging itself is the skill, not a project.

## Key Takeaway
Debugging is a skill, not a talent. Slow down, trace the code like a computer, print the values, narrow down the problem, and use tools like `try`/`except` and the debugger. When stuck, take a break and ask for hints before answers. Bugs are not failure, they are part of learning.