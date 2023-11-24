#Pizza order practice

print("Thank you for choosing Python Pizza Deliveries!")
size = 'S'
add_pepperoni = 'N'
extra_cheese = 'Y'

# 1-version
total = 0 
if size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    total = 29
elif size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'N':
    total = 28
elif size == 'L' and add_pepperoni == 'N' and extra_cheese == 'N':
    total = 25
elif size == 'L' and add_pepperoni == 'N' and extra_cheese == 'Y':
    total = 26 
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    total = 24
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'N':
    total = 23
elif size == 'M' and add_pepperoni == 'N' and extra_cheese == 'N':
    total = 20
elif size == 'M' and add_pepperoni == 'N' and extra_cheese == 'Y':
    total = 21
elif size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    total = 18
elif size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'N':
    total = 17
elif size == 'S' and add_pepperoni == 'N' and extra_cheese == 'N':
    total = 15
elif size == 'S' and add_pepperoni == 'N' and extra_cheese == 'Y':
    total = 16
print(f"Your final bill is: ${total}.")





# second version
bill = 0
if size == 'L':
    bill += 25
elif size == 'M':
    bill += 20
elif size == 'S':
    bill +=15

if add_pepperoni == "Y":
    if size == "L" or size == 'M':
        bill += 3
    elif size == 'S':
        bill += 2

if extra_cheese == "Y":
    bill += 1
print(bill)
