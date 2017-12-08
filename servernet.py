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
         
        mustard = Character(CharacterEnum.ColonelMustard, MustardStart)
        plum = Character(CharacterEnum.ProfessorPlum, PlumStart)
        scarlett = Character(CharacterEnum.MissScarlet, ScarlettStart)
        green =  Character(CharacterEnum.MrGreen, GreenStart)
        white = Character(CharacterEnum.MrsWhite, WhiteStart)
        Peacock = Character(CharacterEnum.MrsPeacock, PeacockStart)
 
        possibleCharacters = [mustard, plum, scarlet, green, white, Peacock] 
        characterList = copy(possibleCharacters) 
        playerList =[]   
        
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

                if msg[1:6] == "Char":
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
        player1 = Player(self.board.playerOneNameSlot.text())
        player2 = Player(self.board.playerTwoNameSlot.text())
        player3 = Player(self.board.playerThreeNameSlot.text())
        player4 = Player(self.board.playerFourNameSlot.text())
        player5 = Player(self.board.playerFiveNameSlot.text())
        player6 = Player(self.board.playerSixNameSlot.text())
        
        playerList = [player1, player2, player3, player4, player5, player6]
        
        turnKeeper = TurnKeeper()
        for player in playerList:
            if player.__str__ != "Waiting...":
                TurnKeeper.add_player(player)
        
        self.board.stackedWidget.setCurrentIndex(1)
        self.board.gameLobby.hide()
        self.board.characterSelection.show()

        '''Connect Character Buttons'''
        self.board.scarlett.clicked.connect(lambda: self.selectCharacter("1Charscarlett"))
        self.board.mustard.clicked.connect(lambda: self.selectCharacter("1Charmustard"))
        self.board.white.clicked.connect(lambda: self.selectCharacter("1Charwhite"))
        self.board.green.clicked.connect(lambda: self.selectCharacter("1Chargreen"))
        self.board.peacock.clicked.connect(lambda: self.selectCharacter("1Charpeacock"))
        self.board.plum.clicked.connect(lambda: self.selectCharacter("1Charplum"))
        
        self.board.continueButton.clicked.connect(self.displayGameBoard)

    def selectCharacter(self, incomingmsg):
        self.board.continueButton.setEnabled(True)
        playerNumber = incomingmsg[0]
        characterInput = incomingmsg[5:]
        
        if characterInput in ['mustard']:
            character = mustard
        elif characterInput in ['scarlett']:
            character = scarlett
        elif characterInput in ['plum']:
            character = plum
        elif characterInput in ['green']:
            character = green
        elif characterInput in ['white']:
            character = white
        elif characterInput in ['peacock']:
            character = Peacock
        else:
            print('Invalid Character Selected')
            character = NULL
            
        if character in possibleCharacters:
            playerTurn.add_character(character)   
            possibleCharacters.remove(character)
            selection = True
        else:
            print('Character already selected')
        '''Assign character to player, send all to clients'''
        '''Disable proper buttons'''

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
        print("after room buttons")
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
