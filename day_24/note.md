File Handling in Python
File handling is an essential part of programming in Python. It allows you to read from and write to files, enabling data persistence.

Opening a File
You can open a file using the open() function:

```python
file = open('filename.txt', 'r')  # 'r' for reading
```

Reading from a File
To read the contents of a file, you can use methods like read(), readline(), or readlines():

```python
content = file.read()  # Reads the entire file
line = file.readline()  # Reads one line
lines = file.readlines()  # Reads all lines into a list
```
Writing to a File
To write to a file, open it in write ('w') or append ('a') mode:

```python
file = open('filename.txt', 'w')  # 'w' for writing
file.write("Hello, World!")
```

Closing a File
Always close the file after you're done to free up system resources:

```python
file.close()
```

Using with Statement
Using the with statement is a best practice as it automatically closes the file:

Example
Here’s a simple example of reading and writing to a file:

Conclusion
File handling in Python is straightforward and powerful, allowing you to manage data efficiently.