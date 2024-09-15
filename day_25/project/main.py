import pandas as pd

# Read the CSV file using pandas
df = pd.read_csv('/home/hvtroller/project/python_100_days/day_25/project/weather_data.csv')

# Extract columns into lists
days = df['day'].tolist()
temperatures = df['temp'].tolist()
weathers = df['condition'].tolist()

# Print the lists joined by '|'
print("|".join(days))
print("|".join(map(str, temperatures)))  # Convert temperatures to strings
print("|".join(weathers))