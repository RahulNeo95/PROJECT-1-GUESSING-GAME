import random

var = random.randint(1, 100)

name = input('Please Enter Your Name: ')
print()
print('WELCOME TO THE GAME', name, "\n")
print('Rules Of The Game: ')
print('The Computer has chosen a Random Number from 1 to 100.')
print('Guess the number chosen by the Computer to Win the Game.')
print('You will get 5 attempts to guess the number and a hint after each guess and get Reward points accordingly.')
print('Player with highest Reward points after 10 games wins THE GAME.\n')

num1 = int(input('Guess the number chosen by the Computer. 1st Guess: '))
if num1 == var:
    print('Congratulations. You have guessed the Correct Number in 1st attempt.')
    print('You get a Reward point of 100 coins.')
elif num1 != var:
    print('Try Again')
    Upper_Range = var + 2
    if Upper_Range <= 100:
        Upper_Range = Upper_Range
    else:
        Upper_Range = 100
    Lower_Range = var - 18
    if Lower_Range >= 0:
        Lower_Range = Lower_Range
    else:
        Lower_Range = 0
    print('Hint1: The Number lies between {1} and {0}\n'.format(Upper_Range, Lower_Range))
    num2 = int(input('Guess the number chosen by the Computer. 2nd Guess: '))
    if num2 == var:

        print('Congratulations. You have guessed the Correct Number in 2nd attempt.')
        print('You get a Reward point of 80 coins.')
    elif num2 != var:
        print('You are Close')
        if var % 2 == 0:
            print('Hint2: The Number is a Even Number\n')
        else:
            print('Hint2: The Number is a Odd Number\n')
        num3 = int(input('Guess the number chosen by the Computer. 3rd Guess: '))
        if num3 == var:
            print('Congratulations. You have guessed the Correct Number in 3rd attempt.')
            print('You get a Reward point of 60 coins.')
        elif num3 != var:
            print('You are Close')
            Upper_Range = var + 1
            if Upper_Range <= 100:
                Upper_Range = Upper_Range
            else:
                Upper_Range = 100
            Lower_Range = var - 9
            if Lower_Range >= 0:
                Lower_Range = Lower_Range
            else:
                Lower_Range = 0
            print('Hint3: The Number lies between {1} and {0}\n'.format(Upper_Range, Lower_Range))
            num4 = int(input('Guess the number chosen by the Computer. 4th Guess: '))
            if num4 == var:
                print('Congratulations. You have guessed the Correct Number in 4th attempt.')
                print('You get a Reward point of 40 coins.')
            elif num4 != var:
                print('You are Close')
                if var % 10 == 0:
                    print('Hint4: The Number ends with 0\n')
                if var % 10 == 1:
                    print('Hint4: The Number ends with 1\n')
                if var % 10 == 2:
                    print('Hint4: The Number ends with 2\n')
                if var % 10 == 3:
                    print('Hint4: The Number ends with 3\n')
                if var % 10 == 4:
                    print('Hint4: The Number ends with 4\n')
                if var % 10 == 5:
                    print('Hint4: The Number ends with 5\n')
                if var % 10 == 6:
                    print('Hint4: The Number ends with 6\n')
                if var % 10 == 7:
                    print('Hint4: The Number ends with 7\n')
                if var % 10 == 8:
                    print('Hint4: The Number ends with 8\n')
                if var % 10 == 9:
                    print('Hint4: The Number ends with 9\n')
                num5 = int(input('Guess the number chosen by the Computer. 5th Guess: '))
                if num5 == var:
                    print()
                    print('Congratulations. You have guessed the Correct Number in 5th attempt.')
                    print('You get a Reward point of 20 coins.')
                    print(
                        'Thank you for playing. Try once more and collect as much Reward points as possible to win THE GAME.')
                else:
                    print()
                    print("Sorry that you couldn't guess the Correct Number.")
                    print('The correct number was', var, end='.')
                    print()
                    print(
                        'Thank you for playing. Try once more and collect as much Reward points as possible to win THE GAME.')
















