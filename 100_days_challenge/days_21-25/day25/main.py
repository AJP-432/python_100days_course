

# with open("weather_data.csv") as weather_data: 
#     data = [line.strip() for line in weather_data.readlines()]

import pandas

# data = pandas.read_csv("weather_data.csv")


# row_monday = data[data.day == "Monday"]
# # Convert C to F
# monday_temp = (int(row_monday.temp)*1.8)+32
# print(monday_temp)


# Go through squirrel csv and count the number of gray, cinnamon, and black 
data = pandas.read_csv("squirrel_data.csv")


gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

color_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# for color in data["Primary Fur Color"]:
#     print(color)
#     if color == "Gray": color_count["Count"][0]+=1 
#     elif color == "Cinnamon": color_count["Count"][1]+=1
#     elif color == "Black": color_count["Count"][2]+=1 
#     else: pass

pandas.DataFrame(color_count).to_csv("squirrel_color_count.csv")


