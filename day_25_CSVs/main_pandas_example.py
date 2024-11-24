import pandas

data = pandas.read_csv("./Day_25_CSVs/weather_data.csv")
print(data["condition"])

data_dict = data.to_dict() #convert the data to dictionary
print(data_dict)

temp_list = data["temp"].to_list() #convert the data to list

average_temp = sum(temp_list)/len(temp_list)
print(data["temp"].max())

monday = data[data.day == "Monday"]
print(monday.temp)