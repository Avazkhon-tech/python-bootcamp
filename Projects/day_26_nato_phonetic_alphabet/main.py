import pandas
new_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        list_words = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only the letters in the alphabet please!")
        generate_phonetic()
    else:
        print(list_words)

generate_phonetic()



