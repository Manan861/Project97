import random
print("Number guessing game")

randomNum=random.randint(1,10)
chances=0
print("Guess a number between 1 and 10")
while chances<5: 
    guess=int(input("Enter your guess: "))
    if guess==randomNum:
        print("Congratulations you won")
        break
    elif guess<randomNum:
        print("Your guess was too low, guess a higher number")
    else:
        print("Your guess was too high, guess a lower number")
    chances=chances+1
if not chances<5:
    print("You lose, the number is:", randomNum)
    


    