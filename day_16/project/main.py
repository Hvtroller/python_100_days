# This is a Coffee Machine project from Day 16 of the 100 days of Python course.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from user import User

def get_user_input():
  name = input("What is your name?: ")
  roll = input("What is your roll:\n1. Normal\n2. Admin\n")
  return User(name, roll)

def handle_admin(user_name):
  print(f"Welcome Admin {user_name}")
  print("1. Check resources")
  print("2. Check profit")
  print("3. Turn off machine")
  admin_input = input("Enter your choice: ")
  print("\n")
  print("*" * 50)
  if admin_input == "1":
    coffee_maker.report()
  elif admin_input == "2":
    money_machine.report()
  elif admin_input == "3":
    print("Turning off machine")
    return False
  
  print("*" * 50)
  return True

def handle_user(user_name, show_welcome=True):
  if show_welcome:
    print(f"Welcome {user_name}")
  print("1. Check menu")
  print("2. Order coffee")
  user_input = input("Enter your choice: ")
  print("\n")
  print("*" * 50)
  if user_input == "1":
    print(menu.get_items())
    print("*" * 50)
    handle_user(user_name, show_welcome=False)
  elif user_input == "2":
    order_name = input("What would you like? (espresso/latte/cappuccino/): ")
    drink = menu.find_drink(order_name)
    if drink:
      if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
    else:
      print("Sorry, that item is not available.")

  print("*" * 50)

  return True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
  user = get_user_input()
  if user.roll == "2":
    is_on = handle_admin(user.get_name())
  else:
    is_on = handle_user(user.get_name())