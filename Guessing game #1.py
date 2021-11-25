"""
guessing game for github 
"""

name = input("Hi! What's your name?")
n1 = 47
guess = int(input(f'Ok. Print your guess from 1 to 100, {name}'))
win = guess == n1
print("You win!"*win + \
      "I win"*(1-win)
      )

