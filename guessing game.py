# I want to make a guessing game and want the user to guess a number between a set of parameters

import random

number = random.randint(1,9)    # Python generates a random number between 1 and 9 inclusive
guess = 0
count = 0

# I want the user to have as many tries as possible to guess the number
# therefore using a while loop that provides indefinite iterations over a block of code
# as long as the while loop conditions remain true

while guess != number and guess != "exit":              # While guess is not equal to the random generated number, the code will continue to loop
    guess = input("Enter a guess between 1 to 9 \n")
    
    if guess == "exit": # to exit the while loop type exit into the input terminal
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it! \nAnd it only took you",count,"tries!") # Breaks the loop and ends the program
        