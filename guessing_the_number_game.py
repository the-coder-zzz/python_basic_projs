import random

print('Enter a number:')
max_num = input('> ')

if max_num.isdigit():
    max_num = int(max_num)
    if max_num <=0:
        print('\nPlease enter a number greater than 0 next time!')
        quit()

else: 
    print('\nPlease enter a number next time!')
    quit()

random_num = random.randint(0, max_num)

guess = 0
while True:
    guess += 1
    the_guess = input('\nEnter a guess: ')
    if the_guess.isdigit():
        the_guess = int(the_guess)
    else:
        print('Please enter a number')
        continue
    if the_guess == random_num:
        print('Congratulations! You made it!')
        break
    elif the_guess > random_num:
        print('Seems close! You were just above the number')
    else:
        print('Seems close! You were just below the number')
print("You got it at", guess, "guess/es")


