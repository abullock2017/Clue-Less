# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from GameBoard import Ui_GameBoard
from GameEnum import RoomEnum, CharacterEnum
from location import Hallway, Room, StartLocation
from CharacterN import Character
from copy import copy
from Player import Player
from TurnKeeper import TurnKeeper
from _overlapped import NULL

def connect_locations(location1, location2):   
    location1.add_connecting_locations(location2)
    location2.add_connecting_locations(location1)

class ServerNet(QWidget, Ui_GameBoard):

    svrsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    clients = set()
    clients_lock = threading.Lock()

    def __init__(self, port, playerName):
        self.host = socket.gethostname() # Get local machine name
        self.ip = socket.gethostbyname(self.host)
        self.port = port             # Reserve a port for your service.
        self.svrsock.bind((self.ip, self.port))        # Bind to the port
        QMainWindow.__init__(self)
        self.board = Ui_GameBoard()
        self.board.setupUi(self)
        self.playerName = playerName
        self.board.playerOneNameSlot.setText(self.playerName)
        self.board.startGameButton.clicked.connect(self.displayCharacterSelection)
        self.characters = [".", ".", ".", ".", ".", "."]
        self.myCharacter = ""
        
        #Create all the rooms on the board
        Study = Room(RoomEnum.Study)
        Hall =  Room(RoomEnum.Hall)
        Lounge = Room(RoomEnum.Lounge)
        Library = Room(RoomEnum.Library)
        BillardRoom = Room(RoomEnum.BilliardRoom)
        DiningRoom = Room(RoomEnum.DiningRoom)
        Conservatory = Room(RoomEnum.Conservatory)
        Ballroom = Room(RoomEnum.Ballroom)
        Kitchen = Room(RoomEnum.Kitchen)
        
        roomList = [Study, Hall, Lounge, Library, BillardRoom, DiningRoom, Conservatory, Ballroom, Kitchen]
        
        #Create the starting locations for the characters
        ScarlettStart = StartLocation('ScarletStart')
        MustardStart = StartLocation('MustardStart')
        PlumStart = StartLocation('PlumStart')
        GreenStart = StartLocation('GreenStart')
        PeacockStart = StartLocation('PeacockStart')
        WhiteStart = StartLocation('WhiteStart')
        
        #Create all the hallways on the board    
        hallway1 = Hallway('hallway 1')
        hallway2 = Hallway('hallway 2')
        hallway3 = Hallway('hallway 3')
        hallway4 = Hallway('hallway 4')
        hallway5 = Hallway('hallway 5')
        hallway6 = Hallway('hallway 6')
        hallway7 = Hallway('hallway 7')
        hallway8 = Hallway('hallway 8')
        hallway9 = Hallway('hallway 9')
        hallway10 = Hallway('hallway 10')
        hallway11 = Hallway('hallway 11')
        hallway12 = Hallway('hallway 12')
        
        #Connect up all the locations on the board together
        connect_locations(Study, hallway1)
        connect_locations(Study, hallway3)
        connect_locations(Study, Kitchen)
        
        connect_locations(Hall, hallway1)
        connect_locations(Hall, hallway2)
        connect_locations(Hall, hallway4)
        
        connect_locations(Lounge, hallway2)
        connect_locations(Lounge, hallway5)
        connect_locations(Lounge, Conservatory)
        
        connect_locations(Library, hallway3)
        connect_locations(Library, hallway6)
        connect_locations(Library, hallway8)
        
        connect_locations(BillardRoom, hallway4)
        connect_locations(BillardRoom, hallway6)
        connect_locations(BillardRoom, hallway7)
        connect_locations(BillardRoom, hallway9)
        
        connect_locations(DiningRoom, hallway5)
        connect_locations(DiningRoom, hallway7)
        connect_locations(DiningRoom, hallway10)
        
        connect_locations(Conservatory, hallway8)
        connect_locations(Conservatory, hallway11)
        
        connect_locations(Ballroom, hallway9)
        connect_locations(Ballroom, hallway11)
        connect_locations(Ballroom, hallway12)
        
        connect_locations(Kitchen, hallway10)
        connect_locations(Kitchen, hallway12)
        
        '''Note that the starting locations are only connected to 1 location
        Add that location does not connect back to the starting location
        Meaning, you can leave the starting area, but not come back in '''  
        
        WhiteStart.add_connecting_locations(hallway12)
        GreenStart.add_connecting_locations(hallway11)
        PeacockStart.add_connecting_locations(hallway8)
        PlumStart.add_connecting_locations(hallway3)
        ScarlettStart.add_connecting_locations(hallway2)
        MustardStart.add_connecting_locations(hallway5)    
        
        self.mustard = Character(CharacterEnum.ColonelMustard, MustardStart)
        
        self.plum = Character(CharacterEnum.ProfessorPlum, PlumStart)
        self.scarlett = Character(CharacterEnum.MissScarlet, ScarlettStart)
        self.green =  Character(CharacterEnum.MrGreen, GreenStart)
        self.white = Character(CharacterEnum.MrsWhite, WhiteStart)
        self.peacock = Character(CharacterEnum.MrsPeacock, PeacockStart)
        
    def listen(self):
        self.svrsock.listen(6)                 # Now wait for client connection.
        #print("Server socket is listening")
        
        while True:
            clnt, addr = self.svrsock.accept()     # Establish connection with client.
            threading.Thread(target = self.listentoclient, args = (clnt, addr)).start() #Start a new thread for each client
        self.svrsock.close()
    
    
    def listentoclient(self, client,address): #This is actioned for each client connection
        with self.clients_lock:
            self.clients.add(client)
        
        while True:
            try:
                msg = client.recv(1024).decode()  #message received from client

                if msg[0:4] == "Join":
                    self.newPlayerJoin(msg)

                if msg[1:5] == "Char":
                    self.selectCharacter(msg)
                    
            
            except:
                client.close()
                return False
        client.close() 


    def newPlayerJoin(self, incomingmsg):

        name = incomingmsg[4:]

        if self.board.playerTwoNameSlot.text() == "Waiting...":
            self.board.playerTwoNameSlot.setText( name )
        elif self.board.playerThreeNameSlot.text() == "Waiting...":
	        self.board.playerThreeNameSlot.setText( name )
        elif self.board.playerFourNameSlot.text() == "Waiting...":
	        self.board.playerFourNameSlot.setText( name )
        elif self.board.playerFiveNameSlot.text() == "Waiting...":
	        self.board.playerFiveNameSlot.setText( name )
        elif self.board.playerSixNameSlot.text() == "Waiting...":
	        self.board.playerSixNameSlot.setText( name ) 

        players = "Join" + self.board.playerOneNameSlot.text() + "," + self.board.playerTwoNameSlot.text() + "," + self.board.playerThreeNameSlot.text() + "," + self.board.playerFourNameSlot.text() + "," + self.board.playerFiveNameSlot.text() + "," + self.board.playerSixNameSlot.text()
        self.sendmsgtoclients( players )

        '''NEEDS TO UPDATE BACKEND!!!'''
	
    def displayCharacterSelection(self):
        self.player1 = Player(self.board.playerOneNameSlot.text())
        self.player2 = Player(self.board.playerTwoNameSlot.text())
        self.player3 = Player(self.board.playerThreeNameSlot.text())
        self.player4 = Player(self.board.playerFourNameSlot.text())
        self.player5 = Player(self.board.playerFiveNameSlot.text())
        self.player6 = Player(self.board.playerSixNameSlot.text())
        
        playerList = [self.player1, self.player2, self.player3, self.player4, self.player5, self.player6]
        
        self.turnKeeper = TurnKeeper()
        for player in playerList:
            if player.__str__ != "Waiting...":
                self.turnKeeper.add_player(player)
        
        self.board.stackedWidget.setCurrentIndex(1)
        self.board.gameLobby.hide()
        self.board.characterSelection.show()

        '''Connect Character Buttons'''
        self.board.scarlett.clicked.connect(lambda: self.selectCharacter("0Charscarlett"))
        self.board.mustard.clicked.connect(lambda: self.selectCharacter("0Charmustard"))
        self.board.white.clicked.connect(lambda: self.selectCharacter("0Charwhite"))
        self.board.green.clicked.connect(lambda: self.selectCharacter("0Chargreen"))
        self.board.peacock.clicked.connect(lambda: self.selectCharacter("0Charpeacock"))
        self.board.plum.clicked.connect(lambda: self.selectCharacter("0Charplum"))
        
        self.board.continueButton.clicked.connect(self.displayGameBoard)

    def selectCharacter(self, incomingmsg):
        self.board.continueButton.setEnabled(True)
        playerNumber = int(incomingmsg[0])
        characterInput = incomingmsg[5:]
        if playerNumber == 0:
            self.myCharacter = characterInput.__str__()

        '''
        self.possibleCharacters = [self.character.mustard, self.character.plum, self.character.scarlet, self.character.green, self.character.white, self.character.Peacock] 
        playerlist = [self.player1, self.player2, self.player3, self.player4, self.player5, self.player6]
       
        if characterInput in ['mustard']:
            character = self.mustard
        elif characterInput in ['scarlett']:
            character = self.scarlett
        elif characterInput in ['plum']:
            character = self.plum
        elif characterInput in ['green']:
            character = self.green
        elif characterInput in ['white']:
            character = self.white
        elif characterInput in ['peacock']:
            character = self.peacock
        else:
            print('Invalid Character Selected')
            character = NULL
        '''
        '''Check this works''''''
        currentplayer = playerlist[playerNumber]
        
        if character in self.possibleCharacters:
            currentplayer.add_character(character)   
            self.possibleCharacters.remove(character)
            selection = True
        else:
            print('Character already selected')
        '''
        '''Assign character to player, send all to clients'''
        '''Disable proper buttons'''
        if characterInput == "mustard":
            self.characters[int(playerNumber)] = "mustard"
        elif characterInput == "white":
            self.characters[int(playerNumber)] = "white"
        elif characterInput == "plum":
            self.characters[int(playerNumber)] = "plum"
        elif characterInput == "peacock":
            self.characters[int(playerNumber)] = "peacock"
        elif characterInput == "scarlett":
            self.characters[int(playerNumber)] = "scarlett"
        elif characterInput == "green":
            self.characters[int(playerNumber)] = "green"
        
        self.board.scarlett.setEnabled(True)
        self.board.mustard.setEnabled(True)
        self.board.white.setEnabled(True)
        self.board.green.setEnabled(True)
        self.board.peacock.setEnabled(True)
        self.board.plum.setEnabled(True)
    
        for char in self.characters:
            print(char)
            if char == "scarlett":
                self.board.scarlett.setEnabled(False)
            elif char == "mustard":
                self.board.mustard.setEnabled(False)
            elif char == "white":
                self.board.white.setEnabled(False)
            elif char == "green":
                self.board.green.setEnabled(False)
            elif char == "peacock":
                self.board.peacock.setEnabled(False)
            elif char == "plum":
                self.board.plum.setEnabled(False)

        if self.myCharacter == 'mustard':
            self.board.mustard.setEnabled(True)
        elif self.myCharacter == 'scarlett':
            self.board.scarlett.setEnabled(True)
        elif self.myCharacter == 'white':
            self.board.white.setEnabled(True)
        elif self.myCharacter == 'green':
            self.board.green.setEnabled(True)
        elif self.myCharacter == 'plum':
            self.board.plum.setEnabled(True)
        elif self.myCharacter == 'peacock':
            self.board.peacock.setEnabled(True)
        
        outgoing = "Char" + self.characters[0].__str__() + "," +self.characters[1].__str__() + "," + self.characters[2].__str__() + "," +self.characters[3].__str__() + "," + self.characters[4].__str__() + "," +self.characters[5].__str__()
        self.sendmsgtoclients(outgoing)


    def displayGameBoard(self):
        self.board.stackedWidget.setCurrentIndex(2)
        self.board.characterSelection.hide()
        self.board.gameBoard.show()
        
        '''Connect ALL the Buttons!!!'''
        #Rooms
        self.board.study.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hall.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayStudyHall.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.lounge.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayHallLounge.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.library.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.billiardRoom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.diningRoom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.conservatory.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.kitchen.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayStudyLibrary.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayHallBilliardRoom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayLoungeDiningRoom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayLibraryConservatory.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayBilliardRoomBallroom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayDiningRoomKitchen.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayLibraryBilliardRoom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayBilliardRoomDiningRoom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayConservatoryBallroom.clicked.connect(lambda: self.moveRoom("msg"))
        self.board.hallwayBallroomKitchen.clicked.connect(lambda: self.moveRoom("msg"))
        # Other Buttons
        
        self.board.makeSuggestionButton.clicked.connect(lambda: self.makeSuggestion)
        self.board.leaveGameButton.clicked.connect(lambda: self.leaveGame)
        self.board.inGameOptionsButton.clicked.connect(lambda: self.options)
        self.board.makeAccusationButton.clicked.connect(lambda: self.makeAccusations)


    def options(self):
        '''To Do'''

    def leaveGame(self):
        '''To Do'''

    def makeAccusation(self, incomingmsg):
        '''To Do'''    

    def makeSuggestion(self, incomingmsg):
        '''To Do'''    

    def moveRoom(self, incomingmsg):
        '''To Do'''

    def nextTurn(self, incomingmsg):
        '''To Do'''

        
    def closeEvent(self, *args, **kwargs):
        self.svrsocket.close()
        return QWidget.closeEvent(self, *args, **kwargs)
    
    #This sends message to all clients, and is server driven
    def sendmsgtoclients(self, msg):
        with self.clients_lock:
            for clt in self.clients:
                clt.sendall(msg.encode())
