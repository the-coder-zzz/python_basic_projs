print('--------------------------')
print('|  WELCOME TO THE QUEST  |')
print('--------------------------')
name = input('\nHello, what is your name: ')

print("\nWelcome", name + "!")

start = input('Would you like to begin your adventure now? (yes/no): ').lower()
if start == "yes":
    print('\nOkay,', name, "let's begin your adventure! Goodluck :)\n")
    quest1 = input('You are on a dark road with two paths going to the right and left, where will you go? (right/left): ').lower()
    if quest1 == 'right':
        quest2 = input('You started walking on the right path and found woods and stones in the ground, would you like to make a fire? (yes/no): ').lower()
        if quest2 == 'yes':
            quest3 = input('You started a fire and made a torch. Now you continued walking and found dead bodies alongside of the way, do you want to continue walking? (yes/no): ').lower()
            if quest3 == 'yes':
                quest4 = input('I admire your bravery, now you reached the end of the road and found a shovel and an x mark on the ground but there is a door ahead. Would you like to enter or use the shovel and find out what is underneath that x? (enter/dig): ')
                if quest4 == 'enter':
                    print('You found a chest and decided to open it. It has lots of gold but it is cursed and you fell for it. You died.')
                    print('You lost!')
                elif quest4 == 'leave':
                    quest5 = input('You entered the door and found a nice village with friendly people. They gifted you resources like gold and shelter and they want you to stay. Would you like to stay there(yes/no): ')
                    if quest5 == 'yes':
                        print('One villager got envious of you and poisoned you while you were asleep and took all of your things.')
                        print('\nYou lost!')
                    elif quest5 == 'no':
                        print('Now you have left, a new adventure awaits you.')
                        print('Congratulations! You won this quest!')
                    else:
                        print('Not a valid option! Try again!')
                else:
                    print('Not a valid option! Try again!')
            elif quest3 == 'no':
                print('You died doing nothing. You lost!')
            else:
                print('Not a valid option! Try again!')
        elif quest2 == 'no':
            print('You died doing nothing. You lost!')
        else:
            print('Not a valid option! Try again!')
    elif quest1 == 'left':
        quest2 = input('You started walking on the left path and found a river, would you like to swim in it? (yes/no): ')
        if quest2 == 'yes':
           print('You were bitten by a river fish monster and died.')
           print('You lost!')
        elif quest2 == 'no':
            quest3 = input('While standing across a river, a monster came. Would you like to fight it? (yes/no)')
            if quest3 == 'yes':
                print("You don't have any weapon yet, you were easily defeated by the monster and died.")
                print('You lost!')
            elif quest3 == 'no':
                print("Since you didin't fight the monster, you were killed by it!")
                print('You lost')
            else:
                print('Not a valid option! Try again!')
        else:
            print('Not a valid option! Try again!')
    else:
        print('Not a valid option! Try again!')
elif start == "no":
    print('Okay, thank you!')
else:
    print('Not a valid option! Try again!')
