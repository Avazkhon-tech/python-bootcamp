# treasure map
line1 = ['','','']
line2 = ['','','']
line3 = ['','','']
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter the position: ")

letter = position[0].lower()
letter_index = 0
if letter == 'a':
    letter_index = 0
elif letter == 'b':
    letter_index = 1
elif letter == 'c':
    letter_index = 2
number = int(position[1])

map[number-1][letter_index] = 'X'
print(f"{line1}\n{line2}\n{line3}")

# # second version
# letter = position[0].lower()
# number = int(position[1])
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)
# map[number-1][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")