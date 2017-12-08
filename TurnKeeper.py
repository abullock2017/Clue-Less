'''
Created on Nov 21, 2017

@author: Zack
'''
from collections import deque
from random import choice

class TurnKeeper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
        print('Adding player {}'.format(player))
        
    
    def generate_turn_order(self):
       
        self.turnOrder = deque()
        #While our set still has player, choose one at random and add them to turn list
        while self.players:
            randomplayer = choice(self.players)
            self.turnOrder.append(randomplayer)
            self.players.remove(randomplayer)
        print(self.turnOrder)
        
    def return_turn_order(self):
        return self.turnOrder  
        
    def next_turn(self):
        nextplayer = self.turnOrder.pop()
        self.turnOrder.appendleft(nextplayer)
        return nextplayer
    
    #Returns True if any players are still playing, meaning they have
    #not lost. Returns false if all players have lost
    def areAnyPlayersLeft(self):
        result = False
        for player in list(self.turnOrder):
            if player.hasLostGame == False:
                result = True
                break
        return result    
        