import pandas

data = pandas.read_csv("D:/100_Days_Code/Day25/weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

avg = sum(temp_list ) / len(temp_list)
print(avg)

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(f"In Fahrenheit {monday_temp_f}")

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amey","James","Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("D:/100_Days_Code/Day25/new_data.csv")