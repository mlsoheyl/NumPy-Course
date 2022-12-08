import random

rand_num = random.randint(1, 100)

guess_number = int(input('I\'m thinking of a number! Try to guess the number I\'m thinking of: '))

while True:
    if guess_number == rand_num:
        play_again = input("That's it! Would you like to play again? (yes/no) ")
        if play_again == 'yes':
            rand_num = random.randint(1, 100)
            guess_number = int(input('I\'m thinking of a number! Try to guess the number I\'m thinking of: '))
            continue
        else:
            break
    elif guess_number < rand_num:
        guess_number = int(input("Too low! Guess again: "))
    else:
        guess_number = int(input("Too high! Guess again: "))
