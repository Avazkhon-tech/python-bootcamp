alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#1st version. this is the combined version of those two functions below
def ceaser (text_input, shift_amount, cipher_direction):
    end_text = ''
    if direction.lower() == "decode":
        shift_amount *= -1
    for letter in text_input:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position < 0:
            new_position = 26 + new_position
        elif new_position > 25:
            new_position = new_position - 26
        end_text += alphabet[new_position]
    print(f"Here is the {cipher_direction}d result: {end_text}")


# 2nd version. it is a bit long but still it works. :)
# def ceaser(text_input, shift_amount, cipher_direction):
#     if cipher_direction.lower() == "encode":
#         cipher_text = ""
#         for letter in text_input:
#             position = alphabet.index(letter)
#             if shift_amount + position >= 25:
#                 position = shift_amount + position - 26
#                 new_position = position
#             else:
#                 new_position = position + shift_amount
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#         print(f"The encoded text is {cipher_text}")
#     elif cipher_direction.lower() == "decode":
#         plain_text = ""
#         for letter in text_input:
#             position = alphabet.index(letter)
#             if position - shift_amount < 0:
#                 new_position = 26 + (position - shift_amount)
#             else:
#                 new_position = position - shift_amount
#             plain_text += alphabet[new_position]
#         print(f"The decoded text is {plain_text}")
ceaser(text, shift, direction)