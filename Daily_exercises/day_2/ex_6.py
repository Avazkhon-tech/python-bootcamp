# bmi calculator

# 1st input: enter height in meters e.g: 1.65
height = input('Height: ')
# 2nd input: enter weight in kilograms e.g: 72
weight = input('Weight: ')


height_float = float(height)
weight_int = int(weight)
bmi = weight_int//(height_float**2)
print(int(bmi))