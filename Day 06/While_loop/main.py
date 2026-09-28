#while something_is_true:
    #repeat this until contion false

#while condition:
    # code to repeat (must be indented)
    # update something so the condition can become False
i = 1
while i <= 5:
    print(i)
    i += 1      # update step, without this the loop never ends
# 1. Check condition
# 2. True  -> run the body, then go back to step 1
# 3. False -> exit the loop


count = 0            # 1. initialization
while count < 3:     # 2. condition
    print("Hi")
    count += 1       # 3. update (increment)


i = 1
while True:
    if i == 4:
        break
    print(i)
    i += 1


i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")

#infinite loop
while True:
    print("Runs forever")   # stop with Ctrl + C

#common example:
password = ""
while password != "abc123":
    password = input("Enter password: ")
print("Access granted")






# pass:	Does nothing. Just a placeholder, the loop carries on normally.
def something():
    pass
# continue:	Skips the rest of the current round and jumps to the next round.:
# break	Stops the whole loop immediately.