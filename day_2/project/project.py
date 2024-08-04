# Output:
# Welcome to Tip Calculator!
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93

print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill = bill + bill * tip_percentage / 100
people = int(input("How many people to split the bill? "))
per_person = total_bill / people

print(f"Each person should pay: ${per_person:.2f}")
