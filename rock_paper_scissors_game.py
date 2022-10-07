import random

user_score = 0
computer_score = 0

options = ['rock', 'paper', 'scissors']

while True:
    print('\nType Rock/Paper/Scissors or Q to quit: ')
    user_pick = input('> ').lower()
    if user_pick == 'q':
        break
    if user_pick not in options:
        print("Please type a correct value\n")
        continue

    random_num = random.randint(0,2)
    computer_pick = options[random_num]

    if user_pick == "rock" and computer_pick == 'scissors':
        print("Congratulations! You won! The computer is scissors.")
        user_score += 1
    elif user_pick == "paper" and computer_pick == 'rock':
        print("Congratulations! You won! The computer is  rock.")
        user_score += 1
    elif user_pick == "scissors" and computer_pick == 'paper':
        print("Congratulations! You won! The computer is paper.")
        user_score += 1
    else:
        print("You lost! Better luck next time!")
        computer_score += 1

print("\nYou won", user_score, "times.")
print('The computer won', computer_score, 'times.' )
print("Goodbye!")
    