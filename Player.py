'''
Created on Nov 19, 2017

@author: Zack
'''
from location import Room
from GameEnum import check_character_input, check_room_input, check_weapon_input
from SuggestionN import  SuggestionClass

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.character = []
        self.face = name
        self.oneMovePerTurn = True
        self.hasLostGame = False
        self.suggestionPossible = False
        self.cardsHeld = []
    
    def __str__(self):
        return self.face
    
    def __repr__(self):
        return self.face    
        
    def add_character(self, character):
        self.character = character
        
    def has_character_already_moved(self):
        return not self.oneMovePerTurn   
    
    def add_clue(self,clue):
        self.cardsHeld.append(clue)
        
    def show_hand(self):
        for cards in self.cardsHeld:
            print(cards)
        
    def move_character(self, requestedLocation):
        #Check to see if the player has already moved this Turn
        if self.oneMovePerTurn == True:
            #if the requested location is acceptable complete the move
            connectingLocations = self.character.available_moves()
            
            for location in connectingLocations:
                if requestedLocation == location.__str__():
                    if self.character.move_location(requestedLocation):
                        #if the move was successful take away the move
                        self.oneMovePerTurn = False
                        if isinstance(self.character.location, Room):
                            self.suggestionPossible = True
                break
            else:
                print("Input location not found")   
        else:
            print('Character has already moved this turn\n') 
            
    def make_suggestion(self):       
        self.suggestionPossible = False
        self.oneMovePerTurn = False
        print('Input Character suggestion')
        characterSuggestion = input()
        while  not check_character_input(characterSuggestion):
            print('Not a valid Suggestion, try again')
            characterSuggestion = input()
        print('Input Weapon suggestion')
        weaponSuggestion = input()
        while not check_weapon_input(weaponSuggestion):
            print('Not a valid Suggestion, try again')
            weaponSuggestion = input()
        roomSuggestion = self.character.location.__str__()
        mySuggestion = SuggestionClass(characterSuggestion, roomSuggestion, weaponSuggestion) 
        return mySuggestion 
                
    def disprove_suggestion(self, suggestion):
        
        possibleDisprovements =[]
        
        for partOfSuggestion in [suggestion.character, suggestion.room, suggestion.weapon]:
            for cards in self.cardsHeld:
                if cards.specific.name == partOfSuggestion:
                    possibleDisprovements.append(cards)
                    
        selection = ('none')
        
        if  possibleDisprovements:      
            Disproved = False
            while not Disproved:
                print('Cards that disprove the suggestion')
                for disprovement in possibleDisprovements:
                    print("{}\n".format(disprovement))
                print('Enter a card')
                selection = input()
                for disprovement in possibleDisprovements:
                    if selection == disprovement.specific.name:
                        Disproved = True                
        else: 
            print("You can not disprove this suggestion\n") 

        return selection
    
    def end_turn(self):
        #Set back the ability to move
        self.oneMovePerTurn = True
        self.suggestionPossible = False
        
    def check_accusation(self, finalEvidence, locationGuess, characterGuess, weaponGuess):
        result = False
        if finalEvidence.weapon.specific.name == weaponGuess:
            print('Weapon guess Correct')
            if finalEvidence.character.specific.name == characterGuess:
                print('Character guess Correct')
                if finalEvidence.room.specific.name == locationGuess:
                    result = True
                    print('Location Guess Correct')
                    
        return result