# Function that allows more than 1 parameter.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Avazkhon", "Tashkent")
greet_with(location='Tashkent', name='Avazkhon')

