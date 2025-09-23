from random import random, randint, uniform

count = 0

for _ in range(1, 6):
    d1 = randint(1, 100)
guess1 = int(input("Guess a number: "))
count += 1
if guess1 == d1:
    print("Congratulations! You guessed the number in {count} attempt(s).")
elif guess1 < d1:
    print("The number is higher")
    newguess = int(input("Guess again: "))
elif guess1 > d1:
    print("The number is lower")
    newguess = int(input("Guess again: "))
    