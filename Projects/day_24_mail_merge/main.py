#TODO: Create a letter using starting_letter.txt
with open("../day_24_mail_merge/input/letters/starting_letter.txt") as file:
    data = file.read()

with open("../day_24_mail_merge/input/names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    name = name.replace('\n', '')
    letter = data.replace('[name]', name)
    with open(f'./output/Readytosend/letter_for_{name}.txt', 'w') as file:
        file.write(letter)




#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp