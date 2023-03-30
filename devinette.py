#jeu de devinette

from random import *
print("Are you ready")
guess=int(input('write a number: '))
number=randint(0, 10)
while number!=guess:
    if guess<number:
        print('Too low')
        guess=int(input("write a number"))
    elif guess>number:
        print('Too high')
        guess=int(input("write a number"))
    else:
        break
    
print("You guessed")