import pandas

data = pandas.read_csv("D:/100_Days_Code/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squireel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squireel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squireel_count)
print(black_squireel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, red_squireel_count, black_squireel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("D:/100_Days_Code/Day25/squirrel_count.csv")