# Class Inheritance in Python

Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another class. This promotes code reusability and establishes a relationship between classes.

## Basic Syntax

```python
class ParentClass:
  def __init__(self):
    self.parent_attribute = "I am a parent"

  def parent_method(self):
    return "This is a method from the parent class"

class ChildClass(ParentClass):
  def __init__(self):
    super().__init__()  # Call the constructor of the parent class
    self.child_attribute = "I am a child"

  def child_method(self):
    return "This is a method from the child class"
```

## Example Usage

```python
child_instance = ChildClass()
print(child_instance.parent_attribute)  # Output: I am a parent
print(child_instance.child_attribute)   # Output: I am a child
print(child_instance.parent_method())   # Output: This is a method from the parent class
print(child_instance.child_method())    # Output: This is a method from the child class
```

## Key Points
- **Single Inheritance**: A class can inherit from one parent class.
- **Multiple Inheritance**: A class can inherit from multiple parent classes.
- **Method Overriding**: A child class can provide a specific implementation of a method that is already defined in its parent class.

## Conclusion

Class inheritance is a powerful feature in Python that allows for the creation of a hierarchical class structure, enabling code reuse and better organization.
