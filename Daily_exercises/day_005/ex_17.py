# finds the highest number in the input

# Input a list of student scores
student_scores = input("Enter the numbers with a indent in between: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_num = 0
for i in student_scores:
  if i > max_num:
    max_num = i
print(f"The highest score in the class is: {max_num}")