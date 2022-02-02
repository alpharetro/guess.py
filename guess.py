import random

guessesTaken = 0

print("Hello, Player! What  might be your name, its the guessing game after all!\n")
name = input()

number = random.randint(1,20)
print("Well, " + name + ", I am thinking of a number between 1 and 20. Guess it!")

for guessesTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print('ur guess lower than the number')

        if guess > number:
            print('yo guess to high')

            if guess == number:
                break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + name + ' ! you guessed my number in ' + guessesTaken + 'guesses!')

    if guess != number:
        number = str(number)
        print('nah, the number i was thinking was ' + number + '.')
