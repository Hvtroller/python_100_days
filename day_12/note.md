**Scope in Python**

In Python, scope refers to the visibility and accessibility of variables, functions, and objects in a particular part of the code. Python has four types of scopes:

1. **Local Scope**: Variables defined within a function are considered to have local scope. They can only be accessed within that function.

2. **Enclosing Scope**: If a function is defined inside another function, the inner function can access variables from the outer function. These variables have an enclosing scope.

3. **Global Scope**: Variables defined outside of any function or class have global scope. They can be accessed from anywhere in the code.

4. **Built-in Scope**: Python provides a set of built-in functions and objects that are available in all scopes. Examples include `print()`, `len()`, and `str()`.

Understanding scope is important for avoiding naming conflicts and managing variable accessibility in your code.

Here are some examples to illustrate the concept of scope in Python:

1. Local Scope:
```python
def my_function():
  x = 10  # Local variable
  print(x)

my_function()  # Output: 10
print(x)  # Error: NameError: name 'x' is not defined
```

2. Enclosing Scope:
```python
def outer_function():
  x = 10  # Enclosing variable

  def inner_function():
    print(x)  # Accessing enclosing variable

  inner_function()

outer_function()  # Output: 10
```

3. Global Scope:
```python
x = 10  # Global variable

def my_function():
  print(x)  # Accessing global variable

my_function()  # Output: 10
```

4. Built-in Scope:
```python
print(len("Hello, World!"))  # Output: 13
```

Understanding scope is crucial for writing clean and maintainable code. It helps prevent variable name clashes and ensures proper variable accessibility.

5. **Constant Scope**: In Python, there is no built-in constant keyword like in some other programming languages. However, by convention, variables that are intended to be treated as constants are typically written in uppercase letters. These variables are usually defined at the global scope and should not be modified throughout the program.

Here's an example of defining and using a constant in Python:

```python
MY_CONSTANT = 3.14

def calculate_area(radius):
  return MY_CONSTANT * radius * radius

print(calculate_area(2))  # Output: 12.56
```

By using uppercase letters and avoiding modifications to the variable, we can indicate that it should be treated as a constant.

