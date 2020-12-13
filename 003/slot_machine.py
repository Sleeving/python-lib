import random


def slot_machine():
    play_again = 'y'
    while play_again == 'y':
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)
        print(num1, num2, num3)
        if num1 == num2 == num3:
            print('Three numbers are the same!')
        elif num1 == num2 or num2 == num3 or num1 == num3:
            print('Two numbers are the same!')
        else:
            print('No numbers were the same. Try again.')
        play_again = input('Would you like to play again? (y or n) ')
        if play_again == 'n':
            break


slot_machine()
