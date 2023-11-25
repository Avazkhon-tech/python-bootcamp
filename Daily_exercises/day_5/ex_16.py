# Input a Python list of student heights
student_heights = [156, 178, 165, 171, 187]
sum = 0
count = 0
for i in student_heights:
    sum += i
    count +=1
average = round(sum/count)
print(f"total height = {sum}")
print(f"number of students = {count}")
print(f"average height = {average}")