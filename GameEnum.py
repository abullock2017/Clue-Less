'''
Created on Nov 18, 2017

@author: Zack
'''
from enum import Enum

class RoomEnum ( Enum ):
    '''
    Enum class of weapons
    '''
    Study = 0
    Hall = 1
    Lounge = 2
    Library = 3
    BilliardRoom = 4
    DiningRoom = 5
    Conservatory = 6
    Ballroom = 7
    Kitchen = 8
    
class CharacterEnum ( Enum ):
    '''
    Enum class of people
    '''
    ColonelMustard = 0
    MissScarlet = 1
    ProfessorPlum = 2
    MrGreen = 3
    MrsWhite = 4
    MrsPeacock = 5

class WeaponEnum ( Enum ):
    '''
    Enum class of weapons
    '''
    Rope = 0
    LeadPipe = 1
    Knife = 2
    Wrench = 3
    Candlestick = 4
    Revolver = 5

def check_room_input(roomInput):
    result = False
    for room in RoomEnum:
        if room.name == roomInput:
            result = True
            break
    return result   

def check_weapon_input(weaponInput):
    result = False
    for weapon in WeaponEnum:
        if weapon.name == weaponInput:
            result = True
            break
    return result   

def check_character_input(characterInput):
    result = False
    for character in CharacterEnum:
        if character.name == characterInput:
            result = True
            break
    return result   