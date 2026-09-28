
from myart import logo
def add(a,b):
    return a+b

# addition = add
# print(addition(3,2)) #5

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b
    
def calculator() :
    is_calculation_continue = True
    print(logo)
    f_num = int(input("What the first number? "))
    while is_calculation_continue:

        print("'+' choose this for addition")
        print("'-' choose this for subtraction")
        print("'*' choose this for multiplication")
        print("'/' choose this for division")

        opp_choice = input("Pick an opperation: ")

        next_num = int(input("What the next number? "))
        pre_cal = 0
        if opp_choice == '+':
            pre_cal = add(f_num,next_num)
            print(f"{f_num} + {next_num} = {add(f_num,next_num)}")
        elif opp_choice == '-':
            pre_cal = subtract(f_num,next_num)
            print(f"{f_num} - {next_num} = {subtract(f_num,next_num)}")
        elif opp_choice == '*':
            pre_cal = multiply(f_num,next_num)
            print(f"{f_num} X {next_num} = {multiply(f_num,next_num)}")
        elif opp_choice == '/':
            pre_cal = divide(f_num,next_num)
            print(f"{f_num} / {next_num} = {divide(f_num,next_num)}")
        choice = input(f"Type 'y' to continue calculating with {pre_cal}, or Type 'n' to start new calculations: " )
        if choice == 'y':
            f_num = pre_cal
        else:
            is_calculation_continue = False
            print("\n"*20)
            calculator()

calculator()

