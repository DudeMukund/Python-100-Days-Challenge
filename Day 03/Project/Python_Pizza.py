print("Welcome to python Delveires!")
size = input("What size pizza do you want? S, M or L:  ")
pepperoni = input("Do you want pepperoni on your pizaa? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")

bill =0
if size =='L':
    bill += 25

elif size == 'M':
    bill += 20

elif size == 'S':
    bill += 15

else:
    print("user typed the wrong input!")

if (pepperoni =="Y" and size =="M"or size=="L"):
    bill += 3
elif pepperoni =="Y":
    bill +=2
if extra_cheese=="Y":
    bill += 1

print(f"your final bill is ${bill}")