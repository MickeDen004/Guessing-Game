"""
guessing game for github 
"""
import random
name = input("Hi! What's your name?")
computer_number = random.randint(1,100)
guess = int(input(f'Ok. Print your guess from 1 to 100, {name}'))
win = guess == computer_number
print("You win!"*win + \
      "I win"*(1-win)
      )
print("Thank you!")
print(f'My nuber was {computer_number}')

