import random
names_string = input("Enter the names : ")
names = names_string.split(', ')
length =  len(names)
random_num = random.randint(0, length- 1)
print(f"{names[random_num]} is going to buy the meal today!")