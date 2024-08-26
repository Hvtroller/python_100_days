# this is program about higer-low game
# there are a dict contains data for the game including name, number_of_followers, description, and country
# the game will show the description and ask the user to guess which one has more followers
# the user will have 3 chances to guess the right answer
# the game will show the number of followers for each account

import random
import data

def select_account():
  return random.choice(data.DATA)

def higher_lower_game():
  print(data.LOGO)
  print("Welcome to the Higher Lower Game!")
  print("I'm thinking of a social media account.")
  print("You have 3 chances to guess which account has more followers.")
  print("Here are the accounts:")
  account1 = select_account()
  account2 = select_account()
  while account1 == account2:
    account2 = select_account()
  print(f"A. {account1['name']} - {account1['description']} - {account1['country']}")
  print(f"B. {account2['name']} - {account2['description']} - {account2['country']}")
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  if (account1['number_of_followers'] > account2['number_of_followers'] and guess == 'A') or (account1['number_of_followers'] < account2['number_of_followers'] and guess == 'B'):
    print("Correct!")
  else:
    print("Incorrect.")
  print(f"The number of followers for {account1['name']} is {account1['number_of_followers']}")
  print(f"The number of followers for {account2['name']} is {account2['number_of_followers']}")

higher_lower_game()
