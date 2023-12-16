import pandas
# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for i in data:
#         if i[1] != 'temp':
#             temperatures.append(int(i[1]))
#     print(temperatures)



# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data['temp'])


# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# average = (sum(temp_list)/len(temp_list))
#
# print(data['temp'].mode())
# print(data['temp'].max())



# # Get Data in Columns
# print(data['condition'])
# print(data.condition)



# # Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print((monday.temp) * 9/5 + 32)



# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("squirrel_count.csv")
fur_colors = data["Primary Fur Color"]
grey_squirrels = len(data[fur_colors == "Gray"])
red_squirrels = len(data[fur_colors == "Cinnamon"])
black_squirrels = len(data[fur_colors == "Black"])
# print(grey_squirrels)
# print(red_squirrels)
# print(black_squirrels)

data_dict = {
    "Fur colors": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_short.csv")








