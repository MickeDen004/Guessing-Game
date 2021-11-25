"""
guessing game for github 
"""

name = input("Hi! What's your name?")
n1 = 47
while True:
    guess = int(input(f'Ok. Print your guess from 1 to 100, {name}'))
    if 0 <guess < 101:
        break
    else:
        print('Try again.')
        continue
win = guess == n1
print("You win!"*win + \
      "I win"*(1-win)
      )

