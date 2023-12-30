from die import *

def attributes():
    '''Randomly Roll for ability scores'''
    #Roll 4d6's and drop lowest number. Add remaining three numbers.
    #Do this 6 times total. Each score can be used once and assigned to an ability
    roll = [roll6() for i in range(0,4)]
    small = min(roll)
    roll.remove(small)
    final = sum(roll)
    return final

def assignp():
    abilities = {
    'Strength' : '',
    'Dexterity' : '',
    'Constitution' : '',
    'Intelligence' : '',
    'Wisdom' : '',
    'Charisma' : ''
    }
    print('Your ability scores are:')
    scores = [attributes() for score in range(0,6)]
    print(scores)

    inp = input('\nContinue with these scores? (Yes / No): ')
    while inp != 'Yes':    

        if inp == 'No':
            print('Re-rolling...\n')

            print('Your ability scores are:')
            scores = [attributes() for score in range(0,6)]
            print(scores)

            inp = input('Continue with these scores? (Yes / No): ')

        else:
            inp = input('\nInvalid input.\nContinue with these scores? (Yes / No): ')
    
    while len(scores) != 0:
        for key in abilities.keys():
            num = int(input('What score would you like to assign to {}?'.format(key)))
            if num in scores:
                abilities.update({key: num})
                scores.remove(num)
            
            else:
                print('Try again!') #FIXME: Make it so the program does not iterate to the next object if the input is invalid

    print()
    for key, value in abilities.items():
        print('{}: {}'.format(key, value))
    inp = input('\nAre you happy with your abiliity scores?')

    if inp == 'Yes':
        return abilities