with open("D:/100_Days_Code/Day25/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


import csv
with open("D:/100_Days_Code/Day25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
print(temperatures)


import pandas
data = pandas.read_csv("D:/100_Days_Code/Day25/weather_data.csv")
print(data)
print(data["temp"])