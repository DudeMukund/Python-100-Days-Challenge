print("Welcome to the tip Calculator! ")
bill = float(input("What was the total bill? $"))

per = int(input("How much tip would you like to give ? 10, 12, or 15? "))
people =int(input("How many people to split the bill? "))
print(f"Each person should pay: ${((bill*per/100)+bill)/people}")