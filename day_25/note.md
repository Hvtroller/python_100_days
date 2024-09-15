# Reading CSV in Python

Python provides several libraries to read CSV files. The most commonly used are `csv` and `pandas`. Below are examples of how to use both.

## Using the `csv` module

```python
import csv

with open('file.csv', mode='r') as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    print(row)
```

## Using `pandas`

```python
import pandas as pd

df = pd.read_csv('file.csv')
print(df)
```

## Conclusion

Choose the method that best fits your needs. The `csv` module is great for simple tasks, while `pandas` offers more powerful data manipulation capabilities.  