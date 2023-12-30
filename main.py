from die import *
from ability import *

print('Hello and welcome to the DND Character Creation!\nLet\'s begin!')

character = {
    'race' : {
        'Dwarf' : ['Hill Dwarf', 'Mountain Dwarf'],
        'Elf' : ['High Elf', 'Wood Elf', 'Dark Elf', 'Sun Elf', 'Moon Elf'],
        'Halfling' : ['Lightfoot', 'Stout'],
        'Human' : ['NA'],
        'Dragonborn' : ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'],
        'Gnome' : ['Forest Gnome', 'Rock Gnome'],
        'Half-Elf' : ['NA'],
        'Half-Orc' : ['NA'],
        'Tiefling' : ['NA']
    },
    'class_type' : {
        'Barbarian' : {
            'Proficiences' : {
                'Armor' : ['Light armor', 'Medium Armor', 'Shields'],
                'Weapons' : ['Simple weapons, Martial weapons'],
                'Tools' : ['None'],
                'Savings Throws' : ['Strength', 'Constitution'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Bard' : {
            'Proficiences' : {
                'Armor' : ['Light armor'],
                'Weapons' : ['Simple weapons', 'Hand crossbows,', 'Longswords', 'Rapiers', 'Shorswords'],
                'Tools' : ['3 musical instruments of your choice'], #FIXME: Figure out how to choose tools and assign to dic
                'Savings Throws' : ['Dexterity', 'Charisma'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Cleric': {
            'Proficiences' : {
                'Armor' : ['Light armor', 'Medium armor', 'Shields'],
                'Weapons' : ['Simple weapons'],
                'Tools' : ['None'],
                'Savings Throws' : ['Wisdon', 'Charisma'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Druid' : {
            'Proficiences' : {
                'Armor' : ['Light armor', 'Medium armor', 'Shields'], #Druids will not wear armor or use shields made of metal
                'Weapons' : ['Clubs', 'Daggers', 'Darts', 'Javelins', 'Maces', 'Quarterstaffs', 'Scimitars', 'Sickles', 'Slings', 'Spears'],
                'Tools' : ['Herbalism kit'],
                'Savings Throws' : ['Intelligence', 'Wisdom'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Fighter' : {
            'Proficiences' : {
                'Armor' : ['All armor, Shields'],
                'Weapons' : ['Simple weapons, Martial weapons'],
                'Tools' : ['None'],
                'Savings Throws' : ['Strength', 'Constitution'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Monk' : {
            'Proficiences' : {
                'Armor' : ['None'],
                'Weapons' : ['Simple weapons', 'Shortswords'],
                'Tools' : ['FIXME'], #Choose 1 artisan's tool or musical instrument
                'Savings Throws' : ['Strength', 'Dexterity'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Paladin' : {
            'Proficiences' : {
                'Armor' : ['All armor', 'Shields'],
                'Weapons' : ['Simple weapons, Martial weapons'],
                'Tools' : ['None'],
                'Savings Throws' : ['Wisdom', 'Charisma'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Ranger' : {
            'Proficiences' : {
                'Armor' : ['Light armor', 'Medium armor', 'Shields'],
                'Weapons' : ['Simple weapons, Martial weapons'],
                'Tools' : ['None'],
                'Savings Throws' : ['Strength', 'Dexterity'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Rogue' : {
            'Proficiences' : {
                'Armor' : ['Light armor'],
                'Weapons' : ['Simple weapons', 'Hand crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
                'Tools' : ['Thieves\' tools'],
                'Savings Throws' : ['Dexterity', 'Intelligence'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Sourcerer' : {
            'Proficiences' : {
                'Armor' : ['None'],
                'Weapons' : ['Darts', 'Daggers', 'Slings', 'Quarterstaffs', 'Light crossbows'],
                'Tools' : ['None'],
                'Savings Throws' : ['Charisma', 'Constitution'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Warlock' : {
            'Proficiences' : {
                'Armor' : ['Light armor'],
                'Weapons' : ['Simple weapons'],
                'Tools' : ['None'],
                'Savings Throws' : ['Wisdom', 'Charisma'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        },
        'Wizard' : {
            'Proficiences' : {
                'Armor' : ['None'],
                'Weapons' : ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light crossbows'],
                'Tools' : ['None'],
                'Savings Throws' : ['Intelligence', 'Wisdom'],
                'Skills' : ['FIXME: Figure out how to choose and assign skills']    #FIXME: Complete skills values
            }
        }
    }
}

races = character['race'].keys()
race = input('Choose your race!\n{}\nRace: '.format(x for x in races))

if 'NA' not in character['race'][race]:
    sub = input('Choose a subrace!\n{}\nSubrace: '.format(character['race'][race]))

print('\nTime to name your character!')
name = input('What should we call it? ')

'''Welcome player and display details on character'''
if 'NA' not in character['race'][race]:
    print('Welcome to the world, {} the {}'.format(name, sub))
else:
    print('Welcome to the world {} the {}'.format(name, race))

print('\nNow let\'s roll for your stats.')
abilities = assignp()