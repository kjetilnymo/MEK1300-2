from random import random, randint, uniform 


answer1 = "YES" 
answer2 = "NO" 

answer = "YES"
 
while answer == answer1:
    d1 = randint(1, 100) 
    count = 0 
    while count < 5: 
        guess1 = int(input("Guess a number: ")) 
        count += 1 
        
        if guess1 == d1: 
            print("Congratulations! You guessed the number in", count, "attempt(s).")
            break
        
        elif guess1 < d1: 
            print("The number is higher") 
        
        else:
            print("The number is lower") 
        
        if count == 5: print("Sorry! You did not manage to guess the number. You have reached the guessing limit. The number was:", d1) 
    
    answer = str(input("Do you want to play again? Type 'YES' or 'NO'. ")).upper()
else:
    print("Okey, see you again.")