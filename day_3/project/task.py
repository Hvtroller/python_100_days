# Task: Write a program that check if a person can ride a rollercoaster based on their height.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Task: Write a program that works out whether if a given number is an odd or even number.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(2))

# Task: Write a program that check if a person can ride a rollercoaster based on their height and age.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    if age >= 12:
        print("You can ride the rollercoaster!")
    else:
        print("Sorry, you have to grow taller before you can ride.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Task: Write a program that calculate the bill for a person can ride a rollercoaster based on their height and age and taking photos.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height >= 120:
    if age >= 12:
        bill = 5
        print("You can ride the rollercoaster!")
    elif age >= 18:
        bill = 12
        print("You can ride the rollercoaster!")
    else:
        bill = 3
        print("Sorry, you have to grow taller before you can ride.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
