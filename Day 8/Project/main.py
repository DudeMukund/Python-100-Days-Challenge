from art import logo 
print(logo)


alp = "abcdefghijklmnopqrstuvwxyz"
def encode(message, shift ):
    '''this fucntion encrypt message acooring to shift'''
    length_message = len(message)
    encoding = ""
    for i in message:
        if i in alp:
            encoding +=  alp[(alp.index(i) + shift) % 26]
        else:
            encoding +=i
    return encoding


def decode(message, shift ):
    '''this fucntion decrypt message acooring to shift'''
    length_message = len(message)
    decoding = ""
    for i in message:
        if i in alp:
            decoding +=  alp[(alp.index(i) - shift) % 26]
        else:
            decoding +=i
    return decoding

# encode("hello zzzzz",1)
# print(decode("if aaa",1))

continue_incoding_and_decoding = True
while(continue_incoding_and_decoding):
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    choice = input().lower()

    print("Type your messages:")
    message= input().lower()

    print("Type the shift number:")
    shift = int(input())

    if choice == "encode":
        print(f"Here's the encoded result {encode(message,shift)}")
    elif choice == "decode":
        print(f"Here's the decoded result {decode(message,shift)}")
    else:
        print("you typed wrong!")


    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    game_choice = input().lower()
    if game_choice == "no":
        print("Good Bye!")
        continue_incoding_and_decoding = False




