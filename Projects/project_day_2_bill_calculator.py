#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = int(input("Enter the total amount of the bill: "))
num_people = int(input("how many people in total: "))
tip = int(input("Choose how much to tip (options: 0%, 10%, 12%): "))

per_person = (bill + bill*tip/100)/num_people
print(per_person) 

