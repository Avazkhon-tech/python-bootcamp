# calculates how many weeks a person has left to live. Programmed assumes that user is expected to live 90 years.

age = input("Enter age: ")

age_int = int(age)
weeks = (90 - age_int)*52
print(f"You have {weeks} weeks left.")