# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from GameBoard import Ui_GameBoard

class ClientNet(QWidget, Ui_GameBoard):

    clntsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    playerNumber = 2
    
    def __init__(self, ipaddress, playerName):
        self.ipaddress = ipaddress
        self.port = 12346  # this is static since we are FWDing to this port
        QMainWindow.__init__(self)
        self.boardgame = Ui_GameBoard()
        self.boardgame.setupUi(self)
	
        self.playerName = playerName
        self.myCharacter = "."
        
        try:
            self.clntsock.connect((ipaddress, self.port))
            threading.Thread(target = self.listen).start()
            
        except:
            print('Error connecting to server')
            self.clntsock.close()
            return False

        msg = "Join" + playerName
        self.sendmsg(msg)
        self.boardgame.stackedWidget.setCurrentIndex(0)
        self.boardgame.gameLobby.show()
        
        self.boardgame.startGameButton.clicked.connect(self.displayCharacterSelection)
        
    def displayCharacterSelection(self):
        self.boardgame.stackedWidget.setCurrentIndex(1)
        self.boardgame.gameLobby.hide()
        self.boardgame.characterSelection.show()
        self.boardgame.continueButton.setEnabled(False)

        '''Connect Character Buttons'''
        self.boardgame.scarlett.clicked.connect(lambda: self.selectCharacterMSG("scarlett"))
        self.boardgame.mustard.clicked.connect(lambda: self.selectCharacterMSG("mustard"))
        self.boardgame.white.clicked.connect(lambda: self.selectCharacterMSG("white"))
        self.boardgame.green.clicked.connect(lambda: self.selectCharacterMSG("green"))
        self.boardgame.peacock.clicked.connect(lambda: self.selectCharacterMSG("peacock"))
        self.boardgame.plum.clicked.connect(lambda: self.selectCharacterMSG("plum"))

        self.boardgame.continueButton.clicked.connect(self.displayGameBoard)

    def selectCharacterMSG(self, character):
        msg = self.playerNumber.__str__() + "Char" + character
        self.myCharacter = character
        self.sendmsg(msg)
        self.boardgame.continueButton.setEnabled(True)

    def displayGameBoard(self):
        self.boardgame.stackedWidget.setCurrentIndex(2)
        self.boardgame.characterSelection.hide()
        self.boardgame.gameboard.show()
        
        '''Connect ALL the Buttons!!!'''
        #Rooms
        self.boardgame.study.clicked.connect(self.moveRoomMSG())
        self.boardgame.hall.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayStudyHall.clicked.connect(self.moveRoomMSG())
        self.boardgame.lounge.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayHallLounge.clicked.connect(self.moveRoomMSG())
        self.boardgame.library.clicked.connect(self.moveRoomMSG())
        self.boardgame.billiardRoom.clicked.connect(self.moveRoomMSG())
        self.boardgame.diningrRoom.clicked.connect(self.moveRoomMSG())
        self.boardgame.conservatory.clicked.connect(self.moveRoomMSG())
        self.boardgame.kitchen.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayStudyLibrary.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwaysHallBilliardRoom.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayLoungeDiningRoom.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayLibraryConservatory.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayBilliardRoomBallroom.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayDiningRoomKitchen.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayLibraryBilliardRoom.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayBilliardRoomDiningRoom.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayConservatoryBallroom.clicked.connect(self.moveRoomMSG())
        self.boardgame.hallwayBallroomKitcchen.clicked.connect(self.moveRoomMSG())
        # Other Buttons
        self.boardgame.makeSuggestionButton.clicked.connect(self.makeSuggestionMSG)
        self.boardgame.leaveGameButton.clicked.connect(self.leaveGameMSG)
        self.boardgame.inGameOptionsButton.clicked.connect(self.options)
        self.boardgame.makeAccusationButton.clicked.connect(self.makeAccusationMSG)

    def entTurnMSG(self):
        '''To Do'''

    def options(self):
        '''To Do'''

    def leaveGameMSG(self):
        '''To Do'''

    def makeAccusationMSG(self):
        '''To Do'''    

    def makeSuggestionMSG(self):
        '''To Do'''        

        
    def moveRoomMSG(self, room):
        '''To Do'''

        
    def sendmsg(self, outMSG):
        encodedMSG = outMSG
        self.clntsock.send(encodedMSG.encode())

    def listen(self):

        #self.boardgame.playerOneNameSlot.setText("Something")
        while True:
            try:
                incomingMSG = (self.clntsock.recv(1024).decode())
                #print(incomingMSG, " received from ", self.ipaddress)
                if incomingMSG != "":
                    print(incomingMSG)
                
                if incomingMSG[0:4] == "Join":
                    self.setPlayerNames( incomingMSG )    
                if incomingMSG[0:4] == "Char":
                    self.setCharacters( incomingMSG )            
                if incomingMSG[0:4] == "Move":
                    self.moveRooms(incomingMSG)



            except:
                print('Lost connection to server')
                self.clntsock.close()
                return False
        self.clntsock.close()

    def accusation(self, incomingmsg):
        '''To Do'''

    def suggestion(self, incomingmsg):
        '''To Do'''

    def leaveGame(self, incomingmsg):
        '''To Do'''


    def moveRooms(self, incomingmsg):
        '''To do'''

    def setCharacters(self, incomingmsg):

    	msg = incomingmsg[4:]
    	names = msg.split(',')
    
    	self.boardgame.scarlett.setEnabled(True)
    	self.boardgame.mustard.setEnabled(True)
    	self.boardgame.white.setEnabled(True)
    	self.boardgame.green.setEnabled(True)
    	self.boardgame.peacock.setEnabled(True)
    	self.boardgame.plum.setEnabled(True)
    
    	for char in names:
            if char == "scarlett":
                self.boardgame.scarlett.setEnabled(False)
            elif char == "mustard":
                self.boardgame.mustard.setEnabled(False)
            elif char == "white":
                self.boardgame.white.setEnabled(False)
            elif char == "green":
                self.boardgame.green.setEnabled(False)
            elif char == "peacock":
                self.boardgame.peacock.setEnabled(False)
            elif char == "plum":
                self.boardgame.plum.setEnabled(False)

            if self.myCharacter == 'mustard':
                self.boardgame.mustard.setEnabled(True)
            elif self.myCharacter == 'scarlett':
                self.boardgame.scarlett.setEnabled(True)
            elif self.myCharacter == 'white':
                self.boardgame.white.setEnabled(True)
            elif self.myCharacter == 'green':
                self.boardgame.green.setEnabled(True)
            elif self.myCharacter == 'plum':
                self.boardgame.plum.setEnabled(True)
            elif self.myCharacter == 'peacock':
                self.boardgame.peacock.setEnabled(True)

    def closeEvent(self, *args, **kwargs):
        self.clntsocket.close()
        return QWidget.closeEvent(self, *args, **kwargs)

        
    def setPlayerNames(self, incomingmsg):
        
        msg = incomingmsg[4:]
        names = msg.split(',')
        
        self.boardgame.playerOneNameSlot.setText(names[0])
        self.boardgame.playerTwoNameSlot.setText(names[1])
        self.boardgame.playerThreeNameSlot.setText(names[2])
        self.boardgame.playerFourNameSlot.setText(names[3])
        self.boardgame.playerFiveNameSlot.setText(names[4])
        self.boardgame.playerSixNameSlot.setText(names[5])
        
        i = 0
        for name in names:
            if name == self.playerName:
                self.playerNumber = i
            i = i + 1
    

