from random import randint

print("Number guessing game\n")

answer1 = "YES" 
answer2 = "NO" 

answer = "YES"
 
while answer == answer1:
    number = randint(1, 100) 
    count = 0 
    while count < 5: 
        bad_guess = input("Guess a number: ")
        if not bad_guess.isdigit() or not (1 <= int(bad_guess) <= 100):
            print("Invalid input. You have to guess a number between 1-100.")
            continue
        guess1 = int(bad_guess)

        count += 1
        
        if guess1 == number: 
            print("Congratulations! You guessed the number in", count, "attempt(s).")
            break
        
        elif guess1 < number: 
            print("The number is higher") 
        
        else:
            print("The number is lower") 
        print("Attempts remaining:", 5 - count,"\n")
        
        if count == 5: print("Sorry! You did not manage to guess the number. You have reached the guessing limit. The number was:", number) 

        
    
    answer = str(input("Do you want to play again? Type 'YES' or 'NO'. ")).upper()
else:
    print("Okey, see you again.")

