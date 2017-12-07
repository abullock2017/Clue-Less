# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from GameBoard import Ui_GameBoard

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

                if msg[0:5] == "Join":
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
        self.sendmsg( players )

        '''NEEDS TO UPDATE BACKEND!!!'''
	
    def displayCharacterSelection(self):
        self.board.stackedWidget.setCurrentIndex(1)
        self.board.gameLobby.hide()
        self.board.characterSelection.show()

        '''Connect Character Buttons'''
        self.board.scarlett.clicked.connect(lambda: self.selectCharacter("1Charscarlett"))
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
        character = incomingmsg[5:]
        
        '''Assign character to player, send all to clients'''
        '''Disable proper buttons'''

    def displayGameBoard(self):
        self.board.stackedWidget.setCurrentIndex(2)
        self.board.characterSelection.hide()
        self.board.gameBoard.show()
        
        '''Connect ALL the Buttons!!!'''
        #Rooms
        self.board.study.clicked.connect(self.moveRoom())
        self.board.hall.clicked.connect(self.moveRoom())
        self.board.hallwayStudyHall.clicked.connect(self.moveRoom())
        self.board.lounge.clicked.connect(self.moveRoom())
        self.board.hallwayHallLounge.clicked.connect(self.moveRoom())
        self.board.library.clicked.connect(self.moveRoom())
        self.board.billiardRoom.clicked.connect(self.moveRoom())
        self.board.diningrRoom.clicked.connect(self.moveRoom())
        self.board.conservatory.clicked.connect(self.moveRoom())
        self.board.kitchen.clicked.connect(self.moveRoom())
        self.board.hallwayStudyLibrary.clicked.connect(self.moveRoom())
        self.board.hallwaysHallBilliardRoom.clicked.connect(self.moveRoom())
        self.board.hallwayLoungeDiningRoom.clicked.connect(self.moveRoom())
        self.board.hallwayLibraryConservatory.clicked.connect(self.moveRoom())
        self.board.hallwayBilliardRoomBallroom.clicked.connect(self.moveRoom())
        self.board.hallwayDiningRoomKitchen.clicked.connect(self.moveRoom())
        self.board.hallwayLibraryBilliardRoom.clicked.connect(self.moveRoom())
        self.board.hallwayBilliardRoomDiningRoom.clicked.connect(self.moveRoom())
        self.board.hallwayConservatoryBallroom.clicked.connect(self.moveRoom())
        self.board.hallwayBallroomKitcchen.clicked.connect(self.moveRoom())
        # Other Buttons
        self.boardgame.makeSuggestionButton.clicked.connect(self.makeSuggestion)
        self.boardgame.leaveGameButton.clicked.connect(self.leaveGame)
        self.boardgame.inGameOptionsButton.clicked.connect(self.options)
        self.boardgame.makeAccusationButton.clicked.connect(self.makeAccusations)


    def options(self):
        '''To Do'''

    def leaveGame(self):
        '''To Do'''

    def makeAccusation(self, incomingmsg):
        '''To Do'''    

    def makeSuggestion(self, incomingmsg):
        '''To Do'''    

    def moveRoom(self, incomingmsg)
        '''To Do'''

    def nextTurn(self, incomingmsg)
        '''To Do'''

        
    def closeEvent(self, *args, **kwargs):
        self.svrsocket.close()
        return QWidget.closeEvent(self, *args, **kwargs)
    
    #This sends message to all clients, and is server driven
    def sendmsgtoclients(self, msg):
        with self.clients_lock:
            for clt in self.clients:
                clt.sendall(msg)