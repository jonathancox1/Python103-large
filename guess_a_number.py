#guess a number game

import random
#number getting game 
#give user 5 chances
attempt = 4
print('You have 5 attempts left')

#accept user input
guess = int(input('Whats the number '))

#create random number
random_number = random.randint(0, 9)

#are there any attempts left?
while attempt > 0:
    #if the guess is incorrect
    while guess != random_number:
        #offer a hint
        hint = input('Would you like a hint? y/n  ')
        print()
        #if user wants a hint, determine if their guess is higher or lower than the random number
        if hint == 'y':
            if guess > random_number:
                print()
                print(f'Hint : {guess} is too high.')
            if guess < random_number:
                print()
                print(f'Hint : {guess} is too low.')
        #inform user of attemts left and promt to guess again
        print(f'You have {attempt} attempts left.')
        guess = int(input('Whats the number '))
        attempt -= 1

        #if user is out of attempts
        if attempt == 0:
            print()
            print(f'You ran out of guesses!')
            again = input('Would you like to play again? y/n  ')
            if again == 'y':
                attempt += 4
                guess = int(input('Whats the number '))
            else:
                print()
                print('Ok Bye.')
                break

    #if guess is correct
    if guess == random_number:
        print('Yes! You win!')
        break
