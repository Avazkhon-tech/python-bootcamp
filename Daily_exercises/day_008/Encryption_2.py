alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if shift + position >= 25:
            position = shift_amount+position - 26
            new_position = position
        else:
            new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by
        if position - shift_amount < 0:
            new_position = 26 + (position - shift_amount)
        else:
            new_position = position - shift_amount
        plain_text += alphabet[new_position]

    print(f"The decoded text is {plain_text}")
# the shift amount and print the decrypted text.

  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'direction' variable. You should be able to test the code to
# encrypt *AND* decrypt a message.

if direction.lower() == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction.lower() == 'decode':
    decrypt(cipher_text= text, shift_amount=shift)
else:
    print("Please enter valid value and run the code again ")
