
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_s = len(data[data["Primary Fur Color"] == "Gray"])
red_s = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_s = len(data[data["Primary Fur Color"] == "Black"])

s_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_s, red_s, black_s]
}
df = pandas.DataFrame(s_dict)
df.to_csv("squirrel_count.csv")