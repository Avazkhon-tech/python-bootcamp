import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser (text_input, shift_amount, cipher_direction):
    end_text = ''
    if direction.lower() == "decode":
        shift_amount *= -1
    for letter in text_input:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here is the {cipher_direction}d result: {end_text}")

print(art.logo)

flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

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


