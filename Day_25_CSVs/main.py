with open("./Day_25_CSVs/weather_data.csv") as weather_data:
    weather_contents = weather_data.readlines()
    print(weather_contents)
    for day in weather_contents[1:]:
        days_list = []
        clean_days = day.strip()
        days_list.append(clean_days)
        weather_day = days_list[0]
        print(weather_day)
        print(clean_days)
