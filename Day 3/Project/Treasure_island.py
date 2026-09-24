
# we us r because we have to show backsalsh(/) also so if we don't use it then it give syntax error 

print (r'''                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')


print("Welcome tp Treasure Island! ")
print("yoy're at a cross road. where do you want to go?")
print("       Type 'left' or 'right'")
cross_choice = input()

print("you've come to lake. There is an island in the middle of the lake.")
print("    Type 'wait' to wait for a boat.  Type 'swim' to swim across")
lake_choice = input()

print("you arrive at the island umharmed. there is house with 3b doors.")
print("  One red, One yellow and one blue. Which colour do you choose? ")
door_choice = input()

if cross_choice =='left':

    if lake_choice == 'wait':
        if  door_choice =='red':
            print("Burn by fire")
            print("Game over!")
        elif door_choice == 'blue':
            print("Eaten by beasts")
            print("Game over!")
        elif door_choice == 'yellow':
            print("You Win!")
        else:
            print("Game Over!")
    
    
    else:
        print("Attacked by trout ")
        print("Game Over!")
else:
    print("Fall into a hole.")
    print("Game Over!")