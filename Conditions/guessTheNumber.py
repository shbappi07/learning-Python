import random

randomNumber = random.randint(10, 20)

for guessTaken in range(1, 20):
    guess = int(input('Enter your Guess: '))
    if guess < 10:
        print('Guess is too low')
    elif guess > 20:
        print('Guess is too high')
    else:
        break
if guess == randomNumber:
    print('Congrats you guessed my number in '+str(guessTaken)+' guesses. ')
else:
    print('OPps your guess is not correct, the number i thought was '+str(randomNumber)+'')
