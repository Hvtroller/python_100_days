# this is a program for Coffee Machine
# it will ask the user to choose what they want to do among the following options:
# - report: print the resources left in the machine
# - espresso: make espresso coffee
# - latte: make latte coffee
# - cappuccino: make cappuccino coffee
# - off: turn off the machine
# the machine has the following resources:
# - water: 300 ml
# - milk: 200 ml
# - coffee: 100 g
# - money: $0
# espresso coffee requires:
# - water: 50 ml
# - coffee: 18 g
# - money: $1.5
# latte coffee requires:
# - water: 200 ml
# - milk: 150 ml
# - coffee: 24 g
# - money: $2.5
# cappuccino coffee requires:
# - water: 250 ml
# - milk: 100 ml
# - coffee: 24 g
# - money: $3.0
# the machine has the following prices:
# - espresso: $1.5
# - latte: $2.5
# - cappuccino: $3.0

resources = {
  'water': 3000,
  'milk': 2000,
  'coffee': 1000,
  'money': 0
}

coffee_menu = {
  'espresso': {
    'water': 50,
    'milk': 0,
    'coffee': 18,
    'price': 1.5
  },
  'latte': {
    'water': 200,
    'milk': 150,
    'coffee': 24,
    'price': 2.5
  },
  'cappuccino': {
    'water': 250,
    'milk': 100,
    'coffee': 24,
    'price': 3.0
  }
}

options = {
  '1': 'report',
  '2': 'espresso',
  '3': 'latte',
  '4': 'cappuccino',
  '5': 'off'
}

history = {
  'espresso': {'count': 0, 'money': 0},
  'latte': {'count': 0, 'money': 0},
  'cappuccino': {'count': 0, 'money': 0}
}

def print_report():
  print(f"""
++++ REPORT +++
Water: {resources['water']} ml
Milk: {resources['milk']} ml
Coffee: {resources['coffee']} g
Money: ${resources['money']}

History:
Espresso: {history['espresso']['count']} - ${history['espresso']['money']}
Latte: {history['latte']['count']} - ${history['latte']['money']}
Cappuccino: {history['cappuccino']['count']} - ${history['cappuccino']['money']}
+++++++++++++++
  """)
  
def make_coffee(coffee):
  for resource in coffee_menu[coffee]:
    if resource == 'price':
      continue 

    if resources[resource] < coffee_menu[coffee][resource]:
      print(f"Sorry, there is not enough {resource}.")
      return

  for resource in coffee_menu[coffee]:
    if resource == 'price':
      resources['money'] += coffee_menu[coffee][resource]
    else:
      resources[resource] -= coffee_menu[coffee][resource]

  history[coffee]['count'] += 1
  history[coffee]['money'] += coffee_menu[coffee]['price']
  print(f"Here is your {coffee}. Enjoy!")
  print(f"Please insert coins of ${coffee_menu[coffee]['price']}")

while True:
  choice = input("""
  What would you like?:
    1. report
    2. espresso
    3. latte
    4. cappuccino
    5. off
""")

  if options[choice] == 'report':
    print_report()
  elif options[choice] == 'off':
    print("Turning off the machine.")
    break
  elif options[choice] in coffee_menu:
    make_coffee(options[choice])
  else:
    print("Invalid choice.")
