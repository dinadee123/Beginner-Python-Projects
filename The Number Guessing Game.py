import random

secret = random.randint(1, 20)

print("Welcome to Guess the Number Game!!!!")
print ("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low!!!")
    elif guess > secret:
        print("Too High!!!")
    else:
        print("CONGRADULATIONS!! The number was", secret)
        break
