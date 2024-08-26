# this is Number gussing game

import random

def select_difficulty():
  print("Select difficulty:")
  print("1. Easy")
  print("2. Medium")
  print("3. Hard")
  choice = int(input("Enter choice: "))
  if choice == 1:
    return 10
  elif choice == 2:
    return 7
  elif choice == 3:
    return 5
  else:
    print("Invalid choice. Defaulting to easy.")
    return 10

def guess_number():
  number = random.randint(1, 100)
  life = select_difficulty()
  print("You have " + str(life) + " guesses to guess the number")
  print("I'm thinking of a number between 1 and 100")
  guess = int(input("Enter your guess: "))
  
  while guess != number:
    if guess < number:
      print("Too low")
    else:
      print("Too high")
    life -= 1
    if life == 0:
      print("You ran out of guesses. The number was " + str(number))
      return
    print("You have " + str(life) + " guesses left")
    print("***********************")
    guess = int(input("Enter your guess: "))
  print("You got it!")

print("""
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|N|u|m|b|e|r|G|u|e|s|s|i|n|g|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

""")
guess_number()