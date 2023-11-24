print("The Love Calculator is calculating your score...")
name1 = input('Enter first person\'s name: ') # What is your name?
name2 = input('Enter second person\'s name: ') # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_total = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_total = l + o + v + e

combined_total = int(f"{first_total}{second_total}")

if combined_total < 10 or combined_total > 90:
    print(f"Your score is {combined_total}, you go together like coke and mentos.")
elif 40 < combined_total < 50:
    print(f"Your score is {combined_total}, you are alright together.")
else:
    print(f"Your score is {combined_total}.")

 