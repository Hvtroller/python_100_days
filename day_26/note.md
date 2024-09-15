# List Comprehension in Python

List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable.

## Basic Syntax

```python
new_list = [expression for item in iterable if condition]
```

### Example

```python
# Create a list of squares for even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
```

## Benefits

- **Conciseness**: Reduces the number of lines of code.
- **Readability**: Often more readable than traditional loops.
- **Performance**: Generally faster than using loops.

## Common Use Cases

- Filtering items from a list.
- Transforming items in a list.
- Creating lists of tuples or dictionaries.

## Conclusion

List comprehensions are a powerful feature in Python that can help you write cleaner and more efficient code.
