A loop in Python allows you to repeatedly execute a block of code. There are two types of loops in Python: `for` loops and `while` loops. 

A `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. Here's an example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
```

This will output:

```
apple
banana
cherry
```

A `while` loop is used to repeatedly execute a block of code as long as a certain condition is true. Here's an example:

```python
count = 0
while count < 5:
  print(count)
  count += 1
```

This will output:

```
0
1
2
3
4
```

Remember to be careful with infinite loops, where the condition is always true and the loop never ends.