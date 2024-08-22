# Hangman Game

This is a step-by-step guide on how to create a Hangman game using Python.

## Step 1: Import necessary modules

In your `project.py` file, start by importing the necessary modules:

```python
import random
```

## Step 2: Define the word list

Next, define a list of words that will be used for the game. You can use a predefined list or create your own. For example:

```python
word_list = ["apple", "banana", "cherry", "durian", "elderberry"]
```

## Step 3: Select a random word

To select a random word from the word list, use the `random.choice()` function:

```python
word = random.choice(word_list)
```

## Step 4: Create the game loop

Create a loop that will run until the game is over. You can use a `while` loop for this:

```python
while True:
  # Game logic goes here
  pass
```

## Step 5: Display the initial state of the game

Inside the game loop, display the initial state of the game. This can be done by printing the number of letters in the word and any initial placeholders. For example:

```python
print(f"The word has {len(word)} letters.")
print("_ " * len(word))
```

## Step 6: Get user input

Prompt the user to guess a letter and store their input in a variable. You can use the `input()` function for this:

```python
guess = input("Guess a letter: ")
```

## Step 7: Check if the letter is in the word

Check if the guessed letter is in the word. You can use an `if` statement for this:

```python
if guess in word:
  print("Correct!")
else:
  print("Wrong!")
```

## Step 8: Update the game state

Inside the game loop, update the game state based on the user's guess. Here are some suggestions on how to handle the different scenarios:

- If the guess is correct:
  - Replace all occurrences of the guessed letter in the word with the actual letter. You can use a combination of `for` loops and conditional statements for this.
  - Print a message to inform the player that their guess was correct.

- If the guess is wrong:
  - Decrement the number of remaining guesses by 1.
  - Print a message to inform the player that their guess was wrong.

- If the player has guessed all the letters correctly:
  - Print a message to inform the player that they have won the game.
  - Break out of the game loop.

- If the player has run out of guesses:
  - Print a message to inform the player that they have lost the game.
  - Break out of the game loop.

You can customize the messages and add more features to enhance the game. Have fun!

## Step 9: Check if the game is over

Check if the game is over by checking if all the letters have been guessed correctly or if the number of remaining guesses is zero. If the game is over, break out of the game loop.

## Step 10: Repeat the game loop

If the game is not over, repeat the game loop and go back to Step 6.

That's it! You have now created a basic Hangman game in Python. Feel free to add more features and enhancements to make it more interesting.
