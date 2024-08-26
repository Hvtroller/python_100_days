# this is calculator project

print(""""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
		
""")

def add(a, b):
		return a + b

def sub(a, b):
		return a - b

def mul(a, b):
		return a * b

def div(a, b):
		return a / b

def mod(a, b):
		return a % b

def is_number(s):
		try:
				float(s)
				return True
		except ValueError:
				return False

operations = {
		"+": add,
		"-": sub,
		"*": mul,
		"/": div,
		"%": mod
}

a = input("Enter first number: ")
b = input("Enter second number: ")
operation = input("Enter operation: ")

if not is_number(a) or not is_number(b):
		print("Both inputs must be numbers.")
elif operation not in operations:
		print("Invalid operation")
else:
		a = float(a)
		b = float(b)
		print(f"{a} {operation} {b} = {operations[operation](a, b)}")
