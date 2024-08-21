# this is rock paper scissors game
import random

def print_choice(choice):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'    ____)____
              ______)
              _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    '''

    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)



choice_a = random.randint(0, 2)
print_choice(choice_a)
choice_b = random.randint(0, 2)
print_choice(choice_b)

if choice_a == choice_b:
    print("It's a draw!")
elif choice_a == 0 and choice_b == 2:
    print("You win!")
elif choice_a == 2 and choice_b == 0:
    print("You lose!")
elif choice_a > choice_b:
    print("You win!")
else:
    print("You lose!")
