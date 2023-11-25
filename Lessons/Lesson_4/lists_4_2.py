# lists
fruits = ['Cherry', 'Apple', 'Pear']

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# calling the items in the list
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[-1])
print(states_of_america[-2])

# changing the items in the list
states_of_america[1] = 'Pencilvania'
print(states_of_america[1])

# adding item to the end of the list
states_of_america.append('Hello land')
states_of_america.extend(['Angelaland', 'Jack Bauer Land'])
print(states_of_america)


# we need to seperate the items in this list into two categories
dirty_dozen_foods = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# nested lists
vegetables = [
    "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"
]

fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes",
    "Peaches", "Cherries", "Pears"
]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)














































