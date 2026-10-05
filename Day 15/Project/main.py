MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resourse_avilable(ingredients):
    flag = False
    for i in ingredients:
        if resources[i] >= ingredients[i]:
            flag = True
        else:
            print(f"Sorry there is not enough {i}")
            flag = False
            break
    return flag


def process_coins():
    print("please insert coins.")
    total = 0.25 * float(input("How many Quarter?: "))
    total += 0.10 * float(input("How many dimes?: "))
    total += 0.05 * float(input("How many nickles?: "))
    total += 0.01 * float(input("How many pennies?: "))
    return total
    

def check_transaction(total, cost):
    global profit
    flag = False
    if cost > total:
        print("Sorry that's not enough money. Money refunded.​")
    elif cost <= total:
        change = total - cost
        profit += cost
        print(f"Here is ${change} dollars in change.")
        flag = True
    return flag


def make_cofee(order , ingredients):
        for i in ingredients:
            resources[i] = resources[i]-ingredients[i]

        print(f"Here is your ☕ {order}. Enjoy!")
        
    
do_you_want_order = True

while(do_you_want_order):
    order = input("What would you like?  (espresso/latte/cappuccino): ").lower()

    if order == "report":
        for i in resources:
            print(f"{i} : {resources[i]}")
        print(f"Profit: ${profit}")

    elif order == "off":
        break

    elif order in MENU:
        drink = MENU[order] # ingredients and #cost
        ingredients = drink["ingredients"] # ingrediants items

        if resourse_avilable(ingredients):
            total = process_coins() # customer money
            if check_transaction(total, drink["cost"]):
                make_cofee(order , ingredients)

    else:
        print("Invalid choice, please try again.")

            







