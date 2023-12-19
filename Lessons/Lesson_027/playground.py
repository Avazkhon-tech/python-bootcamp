"""
# *args
def add(*args):
    print(args[0])
    num_sum = 0
    for i in args:
        num_sum += i
    return num_sum
print(add(5, 5, 5, 5, 5))
"""


# **kwargs
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", colour="white")
print(my_car.colour)