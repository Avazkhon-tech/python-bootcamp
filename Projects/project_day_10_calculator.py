from project_day_10_calculator_logo import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number: "))
    for i in operations:
        print(i)
    flag = True
    while flag:
        operator = input("Pick an operation: ")
        num2 = float(input("What is the next number: "))
        operation_function = operations[operator]
        answer = operation_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        askif = input(f"Type y to continue with {answer} or type n to start a new calculation: ")
        if askif == 'y':
            num1 = answer
        else:
            flag = False
            calculator()
calculator()



























