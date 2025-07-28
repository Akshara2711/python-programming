import random

def guessnumber():
    number = random.randint(1, 100)  
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
                break  
                
        except ValueError:
            print("Please enter a valid number.")

guessnumber()
