character = {
    'race' : { #FIXME: Continue adding traits to each race
        'Dwarf' : {
            'Subrace' : ['Hill Dwarf', 'Mountain Dwarf'],
            'Traits' : {
                'Ability Score Increase' : 'Your Constitution score increases by 2',
                'Size' : 'Medium',
                'Speed' : '25 feet - Not reduced when wearing heavy armor',
                'Darkvision' : 'You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You cannot discern color in darkness, only shades of grey.',
                'Dwarven Resilience' : 'You have an advantage on saving throws against poison, and you have resistance against poison damage',
                'Dwarven Combat Training' : 'You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.',
                'Tool Proficiency' : 'You gain proficiency with the artisans\'s tools of your choice: smith\'s tools, brewer\'s supplies, or mason\'s tools.',
                'Stonecunning' : 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus',
                'Languages' : ['Common', 'Dwarvish'],
            }
        },
        'Elf' : {
            'Subrace' : ['High Elf', 'Wood Elf', 'Dark Elf', 'Sun Elf', 'Moon Elf'],
            'Traits' : {
                'Ability Score Increase' : 'Your Dexterity score increases by 2',
                'Size' : 'Medium',
                'Speed' : '30 feet',
                'Darkvision' : 'You have superior vision oin dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can\'t discern color in darkness, only shades of gray',
                'Keen Senses' : 'You have a proficiency in the Perception skill',
                'Fey Ancestry' : 'You have advantage on saving throws against being charmed, and magic can\'t put you to sleep',
                'Trance' : 'Elves don\'t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. While meditating, you can dream after a fasion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep',
                'Languages' : ['Common', 'Elvish']
            }
        },
        'Halfling' : {
            'Subrace' : ['Lightfoot', 'Stout'],
            'Traits' : {
                'Ability Score Increase' : 'Your Dexterity score increases by 2',
                'Size' : 'Small',
                'Speed' : '25 feet',
                'Lucky' : 'When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll',
                'Brave' : 'You have advantage on saving throws against being frightened',
                'Halfling Nimbleness' : 'You can move through the space of any creature that is of a size larger than yours',
                'Languages' : ['Common', 'Halfing']
            }
        },
        'Human' : {
            'Subrace' : ['NA'],
            'Traits' : {
                'Ability Score Increase' : 'Your ability scores each increase by 1',
                'Size' : 'Medium',
                'Speed' : '30 feet',
                'Languages' : ['Common', '1 extra language of your choice'] #FIXME: Create language selection
            }
        },
        'Dragonborn' : {
            'Subrace' :  ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'],
            'Traits' : {
                'Ability Score Increase' : 'Your Strength score increases by 2, and your Charisma score increases by 1',
                'Size' : 'Medium',
                'Speed' : '30 feet',
                'Draconic Ancestry' : 'You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. Your breath weapon and damage resistance are determined by the dragon type, as shown in the table', #FIXME: Add table
                'Breath Weapon' : 'You can use your action to exhale destructive energy. Your graconic ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapom, you can\'t use it again until you complete a short or long rest.',
                'Damage Resistance' : 'You have resistance to the damage type associated with your draconic ancestry',
                'Languages' : ['Common', 'Draconic']
            }
        },
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
