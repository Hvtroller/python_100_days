# This project is a prime checker project. It is a simple project that checks if a number is prime or not.

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n / 2):
    if n % i == 0:
      return False
  return True

# Test the function
print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
print(is_prime(5)) # True
print(is_prime(6)) # False
print(is_prime(7)) # True
