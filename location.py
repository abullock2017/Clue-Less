'''
Created on Oct 10, 2017

@author: Zack
'''

class Location(object):
    '''
    Areas of the game board that a character can occupy.
    
    TODO:  Start Locations?
    '''
    
    def __init__(self, name):
        self.roomType = name
        self.connectingLocations = set()
        
    def add_connecting_locations(self, connectingLocation):
        self.connectingLocations.add(connectingLocation)
        
    def available_to_enter(self):
        pass
      
    
    def show_connecting_locations(self):
        # Simple function for test
        for k in self.connectingLocations:
            print( "{} is connected to {}".format(self, k))
            
    def return_connecting_locations(self):
        return self.connectingLocations

class Hallway(Location):
    '''
    Connections between rooms.
    '''

    def __init__(self, hallwayName):
        '''
        Constructor
        '''
        super().__init__(hallwayName)
        self.occupied = False
        
    def __str__(self):
        return self.roomType

    def available_to_enter(self):
        #Return true if the hallway is not already occupied
        if self.occupied == False:
            result = True
        else:
            result = False
        return result
         
        

        
class Room(Location):
    '''
   Locations that characters can occupy and make suggestions in.
    '''
    
    def __init__(self, roomname):
        '''
        Constructor
        '''
        super().__init__(roomname)
        
    def __str__(self):
        return self.roomType.name
    
    def available_to_enter(self):
        return True

class StartLocation(Location):
    '''
    Connections between rooms.
    '''

    def __init__(self, startLocation):
        '''
        Constructor
        '''
        super().__init__(startLocation)
        
    def __str__(self):
        return self.roomType
    