import pandas

data = pandas.read_csv("./day_25_CSVs/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") #put your location of the file
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(f"Gray squirrels are: {gray_squirrels}\nCinammon squirrels are: {cinnamon_squirrels}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./day_25_CSVs/squirrel/squirrel_count.csv")