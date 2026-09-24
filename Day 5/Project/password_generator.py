l = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = list(l)
number = ["0","1","2","3","4","5","6","7","8","9"]
symbol = ["~","@","!","#","%","^","$","&","*","-","+"]
import random as r

print("Welcome to the Py Password Genorator: ")
print("How many letters would you like in your password?")
let = int(input())
print("How many symbols would you like?")
sym = int(input())
print("How many numbers would you like?")
num = int(input())

password = ""

for i in range(1,let+1):
    password += r.choice(alpha)

for i in range(1,sym+1):
    password += r.choice(symbol)

for i in range(1,num+1):
    password += r.choice(number)

pass_list = list(password)
hard_password =""
for i in range(len(pass_list)+1):
    hard_password += r.choice(password)
print(f"Easy Password: {password}")
print(f"hard Password: {hard_password}")



