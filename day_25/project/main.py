import csv

# Open the day_25/project/weather_data.csv and print the temperature of the city in the first row.

days = []
temperatures = []
weathers = []

with open('/home/hvtroller/project/python_100_days/day_25/project/weather_data.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header
    
    for row in reader:
        days.append(row[0])
        temperatures.append(row[1])
        weathers.append(row[2])

print("|".join(days))
print("|".join(temperatures))
print("|".join(weathers))