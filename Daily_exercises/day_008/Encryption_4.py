import Encryption_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser (text_input, shift_amount, cipher_direction):
    end_text = ''
    if direction.lower() == "decode":
        shift_amount *= -1
    for letter in text_input:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here is the {cipher_direction}d result: {end_text}")


#TODO-1: Import and print the logo from art.py when the program starts.
print(Encryption_logo.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    #Hint: Think about how you can use the modulus (%).
    ceaser(text_input= text, shift_amount= shift, cipher_direction= direction)
    flag_2 = True
    while flag_2:
        determiner = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
        if determiner == 'yes':
            flag_2 = False
            continue
        elif determiner == 'no':
            flag = False
            flag_2 = False
            print("Goodbye")
        else:
            print("Please enter valid value. 'yes' or 'no'")
















