import random
import string

# this is a password generator
# it will generate a password of length from user input
# it will also ask user if they want to include how many special characters
# it will also ask user if they want to include how many numbers

# Generate a password with choices from separate pools
def generate_password(length, num_special_chars, num_numbers):
  # Define the characters to choose from
  letters = string.ascii_letters
  special_chars = string.punctuation
  numbers = string.digits

  # Create separate pools of characters to choose from
  letter_pool = random.choices(letters, k=length - num_special_chars - num_numbers)
  special_char_pool = random.choices(special_chars, k=num_special_chars)
  number_pool = random.choices(numbers, k=num_numbers)
  password_pool = letter_pool + special_char_pool + number_pool

  # Combine the pools to create the password
  password = "".join(random.sample(password_pool, length))

  return password

# Get user input for password length, number of special characters, and number of numbers
length = int(input("Enter the length of the password: "))
num_special_chars = int(input("Enter the number of special characters to include: "))
num_numbers = int(input("Enter the number of numbers to include: "))

# Generate the password
password = generate_password(length, num_special_chars, num_numbers)

# Print the generated password
print("Generated Password:", password)
