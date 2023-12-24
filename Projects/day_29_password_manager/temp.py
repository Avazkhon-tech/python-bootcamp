from random import *

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = []
    nr_letters = randint(8,10)
    nr_symbols = randint(2,4)
    nr_numbers = randint(2, 4)

    password = [choice(letters) for _ in range(nr_letters)] + [choice(symbols) for _ in range(nr_symbols)] + [choice(numbers) for _ in range(nr_numbers)]
    shuffle(password)
    password_new = ''.join(password)
    print(password_new)


generate_password()