import random

number = random.randint(1,100)

attempts = 0
max_attempts = 7

print("Guess the number from 1 to 100")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempts : {attempts + 1}: enter your guess : "))
        attempts = attempts + 1

        if guess == number:
            print("🎉 Correct ! you guessed it")

        elif guess < number :
            print("Too low")

        else:
            print("Too high")

    except:
        print("Please enter valid number...")

        if attempts == max_attempts and guess != number:
            print(f"Out of attempts !, The number was {number}")