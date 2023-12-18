list_of_strings = input().split(',')
integer_numbers = [int(n) for n in list_of_strings]
result = [n for n in integer_numbers if n % 2 == 0]
print(result)
