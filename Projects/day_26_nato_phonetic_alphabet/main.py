import pandas
#TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
list_words = [new_dict[letter] for letter in user_input]
print(list_words)

