# Dictionary in Python

In Python, a dictionary is an unordered collection of key-value pairs. It is also known as an associative array or a hash map. Dictionaries are mutable, which means you can modify, add, or remove items after they are created.

To create a dictionary, you can use curly braces `{}` or the `dict()` constructor. Here's an example:

```python
# Creating a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
```

In the above example, `"name"`, `"age"`, and `"city"` are the keys, and `"John"`, `25`, and `"New York"` are the corresponding values.

You can access the values in a dictionary by using the keys. Here's how you can access the value associated with the key `"name"`:

```python
# Accessing a value
name = my_dict["name"]
print(name)  # Output: John
```

You can also modify the values in a dictionary by assigning a new value to a key:

```python
# Modifying a value
my_dict["age"] = 30
print(my_dict)  # Output: {"name": "John", "age": 30, "city": "New York"}
```

To add a new key-value pair to a dictionary, you can simply assign a value to a new key:

```python
# Adding a new key-value pair
my_dict["occupation"] = "Engineer"
print(my_dict)  # Output: {"name": "John", "age": 30, "city": "New York", "occupation": "Engineer"}
```

To remove a key-value pair from a dictionary, you can use the `del` keyword:

```python
# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {"name": "John", "age": 30, "occupation": "Engineer"}
```

Dictionaries are a powerful data structure in Python that allow you to store and retrieve data efficiently using keys. They are commonly used in various programming tasks, such as storing configuration settings, mapping values, and more.
