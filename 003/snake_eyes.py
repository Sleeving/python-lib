import random


def snake_eyes():
    tries = 0
    while True:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(dice1, dice2)
        if dice1 == 1 and dice2 == 1:
            print(f'It took {tries} tries to get a snake eyes.')
            play_again = input('Do you wish to play again? (y or n) ')
            if play_again == 'y':
                tries = 0
                continue
            else:
                break
        tries += 1


snake_eyes()
