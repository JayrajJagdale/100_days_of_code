import pandas

data = pandas.read_csv("D:/100_Days_Code/Day25/weather_data.csv")

monday = data[data.day == "Tuesday"]
print(monday)
monday_temp = monday.condition[1]
print(monday_temp)