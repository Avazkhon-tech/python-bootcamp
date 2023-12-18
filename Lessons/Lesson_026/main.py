# # List comprehension
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# new_list = [n + 1 for n in numbers]
# print(new_list)


# # with strings
# name = "Avazkhon"
# new_list = [letter for letter in name]
# print(new_list)

# numbers_list = [n * 2 for n in range(1,5)]
# print(numbers_list)


# # Conditional list comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
#
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


# # Dictionary Comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {'Alex': 2,
#                   'Beth': 52,
#                   'Caroline': 23,
#                   'Dave': 63,
#                   'Eleanor': 80,
#                   'Freddie': 13}
#
# passes_students = {student: score for (student, score) in students_scores.items() if score > 60}
# print(passes_students)



student_dict = {
    'student': ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for key, value in student_data_frame.items():

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)




