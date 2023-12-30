from ability import attributes

class Character:
    """Represent a character's traits"""

    def __init__(self, name, race, char_class, size='Medium', gold=0, level=1, xp=0, speed=30, strength=0, dexterity=0,
                 constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.size = size
        self.gold = gold
        self.level = level
        self.xp = xp
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        # Adjust speed and size based on race
        if self.race == 'Halfling':
            self.size = 'Small'
            self.speed = 25
        elif self.race == 'Gnome':
            self.size = 'Small'
            self.speed = 25

    def adjust_scores(self):
        # Adjust ability scores individually
        if self.strength == 1:
            self.strength -= 5
        elif (self.strength > 1) and (self.strength < 4):
            self.strength -= 4
        elif (self.strength > 3) and (self.strength < 6):
            self.strength -= 3
        elif (self.strength > 5) and (self.strength < 8):
            self.strength -= 2
        elif (self.strength > 7) and (self.strength < 10):
            self.strength -= 1
        elif (self.strength > 9) and (self.strength < 12):
            self.strength += 0
        elif (self.strength > 11) and (self.strength < 14):
            self.strength += 1
        elif (self.strength > 13) and (self.strength < 16):
            self.strength += 2
        elif (self.strength > 15) and (self.strength < 18):
            self.strength += 3
        elif (self.strength > 17) and (self.strength < 20):
            self.strength += 4
        elif (self.strength > 19) and (self.strength < 22):
            self.strength += 5
        elif (self.strength > 21) and (self.strength < 24):
            self.strength += 6
        elif (self.strength > 23) and (self.strength < 26):
            self.strength += 7
        elif (self.strength > 25) and (self.strength < 28):
            self.strength += 8
        elif (self.strength > 27) and (self.strength < 30):
            self.strength += 9
        elif self.strength == 30:
            self.strength += 10

        if self.dexterity == 1:
            self.dexterity -= 5
        elif (self.dexterity > 1) and (self.dexterity < 4):
            self.dexterity -= 4
        elif (self.dexterity > 3) and (self.dexterity < 6):
            self.dexterity -= 3
        elif (self.dexterity > 5) and (self.dexterity < 8):
            self.dexterity -= 2
        elif (self.dexterity > 7) and (self.dexterity < 10):
            self.dexterity -= 1
        elif (self.dexterity > 9) and (self.dexterity < 12):
            self.dexterity += 0
        elif (self.dexterity > 11) and (self.dexterity < 14):
            self.dexterity += 1
        elif (self.dexterity > 13) and (self.dexterity < 16):
            self.dexterity += 2
        elif (self.dexterity > 15) and (self.dexterity < 18):
            self.dexterity += 3
        elif (self.dexterity > 17) and (self.dexterity < 20):
            self.dexterity += 4
        elif (self.dexterity > 19) and (self.dexterity < 22):
            self.dexterity += 5
        elif (self.dexterity > 21) and (self.dexterity < 24):
            self.dexterity += 6
        elif (self.dexterity > 23) and (self.dexterity < 26):
            self.dexterity += 7
        elif (self.dexterity > 25) and (self.dexterity < 28):
            self.dexterity += 8
        elif (self.dexterity > 27) and (self.dexterity < 30):
            self.dexterity += 9
        elif self.dexterity == 30:
            self.dexterity += 10

        if self.constitution == 1:
            self.constitution -= 5
        elif (self.constitution > 1) and (self.constitution < 4):
            self.constitution -= 4
        elif (self.constitution > 3) and (self.constitution < 6):
            self.constitution -= 3
        elif (self.constitution > 5) and (self.constitution < 8):
            self.constitution -= 2
        elif (self.constitution > 7) and (self.constitution < 10):
            self.constitution -= 1
        elif (self.constitution > 9) and (self.constitution < 12):
            self.constitution += 0
        elif (self.constitution > 11) and (self.constitution < 14):
            self.constitution += 1
        elif (self.constitution > 13) and (self.constitution < 16):
            self.constitution += 2
        elif (self.constitution > 15) and (self.constitution < 18):
            self.constitution += 3
        elif (self.constitution > 17) and (self.constitution < 20):
            self.constitution += 4
        elif (self.constitution > 19) and (self.constitution < 22):
            self.constitution += 5
        elif (self.constitution > 21) and (self.constitution < 24):
            self.constitution += 6
        elif (self.constitution > 23) and (self.constitution < 26):
            self.constitution += 7
        elif (self.constitution > 25) and (self.constitution < 28):
            self.constitution += 8
        elif (self.constitution > 27) and (self.constitution < 30):
            self.constitution += 9
        elif self.constitution == 30:
            self.constitution += 10

        if self.intelligence == 1:
            self.intelligence -= 5
        elif (self.intelligence > 1) and (self.intelligence < 4):
            self.intelligence -= 4
        elif (self.intelligence > 3) and (self.intelligence < 6):
            self.intelligence -= 3
        elif (self.intelligence > 5) and (self.intelligence < 8):
            self.intelligence -= 2
        elif (self.intelligence > 7) and (self.intelligence < 10):
            self.intelligence -= 1
        elif (self.intelligence > 9) and (self.intelligence < 12):
            self.intelligence += 0
        elif (self.intelligence > 11) and (self.intelligence < 14):
            self.intelligence += 1
        elif (self.intelligence > 13) and (self.intelligence < 16):
            self.intelligence += 2
        elif (self.intelligence > 15) and (self.intelligence < 18):
            self.intelligence += 3
        elif (self.intelligence > 17) and (self.intelligence < 20):
            self.intelligence += 4
        elif (self.intelligence > 19) and (self.intelligence < 22):
            self.intelligence += 5
        elif (self.intelligence > 21) and (self.intelligence < 24):
            self.intelligence += 6
        elif (self.intelligence > 23) and (self.intelligence < 26):
            self.intelligence += 7
        elif (self.intelligence > 25) and (self.intelligence < 28):
            self.intelligence += 8
        elif (self.intelligence > 27) and (self.intelligence < 30):
            self.intelligence += 9
        elif self.intelligence == 30:
            self.intelligence += 10

        if self.wisdom == 1:
            self.wisdom -= 5
        elif (self.wisdom > 1) and (self.wisdom < 4):
            self.wisdom -= 4
        elif (self.wisdom > 3) and (self.wisdom < 6):
            self.wisdom -= 3
        elif (self.wisdom > 5) and (self.wisdom < 8):
            self.wisdom -= 2
        elif (self.wisdom > 7) and (self.wisdom < 10):
            self.wisdom -= 1
        elif (self.wisdom > 9) and (self.wisdom < 12):
            self.wisdom += 0
        elif (self.wisdom > 11) and (self.wisdom < 14):
            self.wisdom += 1
        elif (self.wisdom > 13) and (self.wisdom < 16):
            self.wisdom += 2
        elif (self.wisdom > 15) and (self.wisdom < 18):
            self.wisdom += 3
        elif (self.wisdom > 17) and (self.wisdom < 20):
            self.wisdom += 4
        elif (self.wisdom > 19) and (self.wisdom < 22):
            self.wisdom += 5
        elif (self.wisdom > 21) and (self.wisdom < 24):
            self.wisdom += 6
        elif (self.wisdom > 23) and (self.wisdom < 26):
            self.wisdom += 7
        elif (self.wisdom > 25) and (self.wisdom < 28):
            self.wisdom += 8
        elif (self.wisdom > 27) and (self.wisdom < 30):
            self.wisdom += 9
        elif self.wisdom == 30:
            self.wisdom += 10

        if self.charisma == 1:
            self.charisma -= 5
        elif (self.charisma > 1) and (self.charisma < 4):
            self.charisma -= 4
        elif (self.charisma > 3) and (self.charisma < 6):
            self.charisma -= 3
        elif (self.charisma > 5) and (self.charisma < 8):
            self.charisma -= 2
        elif (self.charisma > 7) and (self.charisma < 10):
            self.charisma -= 1
        elif (self.charisma > 9) and (self.charisma < 12):
            self.charisma += 0
        elif (self.charisma > 11) and (self.charisma < 14):
            self.charisma += 1
        elif (self.charisma > 13) and (self.charisma < 16):
            self.charisma += 2
        elif (self.charisma > 15) and (self.charisma < 18):
            self.charisma += 3
        elif (self.charisma > 17) and (self.charisma < 20):
            self.charisma += 4
        elif (self.charisma > 19) and (self.charisma < 22):
            self.charisma += 5
        elif (self.charisma > 21) and (self.charisma < 24):
            self.charisma += 6
        elif (self.charisma > 23) and (self.charisma < 26):
            self.charisma += 7
        elif (self.charisma > 25) and (self.charisma < 28):
            self.charisma += 8
        elif (self.charisma > 27) and (self.charisma < 30):
            self.charisma += 9
        elif self.charisma == 30:
            self.charisma += 10

        # Adjust ability scores based on race
        # Adjust strength
        if ((self.race == 'Dragonborn') or (self.race == 'Half-Orc')
                or (self.race == 'Mountain Dwarf')):
            self.strength += 2
        elif self.race == 'Human':
            self.strength += 1

        # Adjust dexterity
        if (self.race == 'Elf') or (self.race == 'Halfling'):
            self.dexterity += 2
        elif (self.race == 'Human') or (self.race == 'Forest Gnome'):
            self.dexterity += 1

        # Adjust constitution
        if self.race == 'Dwarf':
            self.constitution += 2
        elif ((self.race == 'Stout Halfling') or (self.race == 'Rock Gnome') or (self.race == 'Half-Orc')
              or (self.race == 'Human')):
            self.constitution += 1

        # Adjust intelligence
        if (self.race == 'High Elf') or (self.race == 'Tiefling') or (self.race == 'Human'):
            self.intelligence += 1
        elif self.race == 'Gnome':
            self.intelligence += 2

        # Adjust wisdom
        if (self.race == 'Hill Dwarf') or (self.race == 'Human') or (self.race == 'Wood Elf'):
            self.wisdom += 1

        # Adjust charisma
        if ((self.race == 'Drow') or (self.race == 'Lightfoot Halfling') or (self.race == 'Dragonborn')
                or (self.race == 'Human')):
            self.charisma += 1
        elif (self.race == 'Tiefling') or (self.race == 'Half-Elf'):
            self.charisma += 2

    def show_traits(self):  # FIXME: MAKE A BETTER NAME
        print("TRAITS:\n")
        if self.char_class == 'Barbarian':
            print("Armor : Light armor, Medium Armor, Shields\n"
                  "Weapons : Simple weapons, Martial weapons\n"
                  "Tools : None\n"
                  "Savings Throws : Strength, Constitution\n"
                  "Skills : FIXME: Figure out how to choose and assign skills\n")

        elif self.char_class == 'Bard':
            print('Armor : Light armor\n'
                  'Weapons : Simple weapons, Hand crossbows, Longswords, Rapiers, Shortswords\n'
                  'Tools : 3 musical instruments of your choice\n'  # FIXME: Figure out how to choose tools and assign to dic
                  'Savings Throws : Dexterity, Charisma\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Cleric':
            print('Armor : Light armor, Medium armor, Shields\n'
                  'Weapons : Simple weapons\n'
                  'Tools : None\n'
                  'Savings Throws : Wisdom, Charisma\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Druid':
            print(
                'Armor : Light armor, Medium armor, Shields'  # Druids will not wear armor or use shields made of metal
                'Weapons : Clubs, Daggers, Darts, Javelins, Maces, Quarterstaffs, Scimitars, Sickles, Slings, Spears'
                'Tools : Herbalism kit'
                'Savings Throws : Intelligence, Wisdom'
                'Skills : FIXME: Figure out how to choose and assign skills')

        elif self.char_class == 'Fighter':
            print('Armor: All armor, Shields\n'
                  'Weapons: Simple weapons, Martial weapons\n'
                  'Tools: None\n'
                  'Savings Throws: Strength, Constitution\n'
                  'Skills: FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Monk':
            print('Armor : All armor, Shields\n'
                  'Weapons : Simple weapons, Martial weapons\n'
                  'Tools : None\n'
                  'Savings Throws : Strength, Constitution\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Paladin':
            print('Armor : All armor, Shields\n'
                  'Weapons : Simple weapons, Martial weapons\n'
                  'Tools : None\n'
                  'Savings Throws : Wisdom, Charisma\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Ranger':
            print('Armor : Light armor, Medium armor, Shields\n'
                  'Weapons : Simple weapons, Martial weapons\n'
                  'Tools : None\n'
                  'Savings Throws : Strength, Dexterity\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Rogue':
            print('Armor : Light armor\n'
                  'Weapons : Simple weapons, Hand crossbows, Longswords, Rapiers, Shortswords\n'
                  'Tools : Thieves\' tools\n'
                  'Savings Throws : Dexterity, Intelligence\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Sourcerer':
            print('Armor : None\n'
                  'Weapons : Darts, Daggers, Slings, Quarterstaffs, Light crossbows\n'
                  'Tools : None\n'
                  'Savings Throws : Charisma, Constitution\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Warlock':
            print('Armor : Light armor\n'
                  'Weapons : Simple weapons\n'
                  'Tools : None\n'
                  'Savings Throws : Wisdom, Charisma\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')

        elif self.char_class == 'Wizard':
            print('Armor : None\n'
                  'Weapons : Daggers, Darts, Slings, Quarterstaffs, Light crossbows\n'
                  'Tools : None\n'
                  'Savings Throws : Intelligence, Wisdom\n'
                  'Skills : FIXME: Figure out how to choose and assign skills\n')
