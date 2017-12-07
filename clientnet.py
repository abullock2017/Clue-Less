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

        '''Connect Character Buttons'''
        self.boardgame.scarlett.clicked.connect(lambda: self.selectCharacter("scarlett"))
        self.boardgame.mustard.clicked.connect(lambda: self.selectCharacter("mustard"))
        self.boardgame.white.clicked.connect(lambda: self.selectCharacter("white"))
        self.boardgame.green.clicked.connect(lambda: self.selectCharacter("green"))
        self.boardgame.peacock.clicked.connect(lambda: self.selectCharacter("peacock"))
        self.boardgame.plum.clicked.connect(lambda: self.selectCharacter("plum"))

        self.boardgame.continueButton.clicked.connect(self.displayGameBoard)

    def selectCharacter(self, character):
        msg = self.playerNumber + "Char" + character
        self.sendmsg(msg)
        self.boardgame.continueButton.setEnabled(True)


    def displayGameBoard(self):
        self.boardgame.stackedWidget.setCurrentIndex(2)
        self.boardgame.characterSelection.hide()
        self.boardgame.gameboard.show()
        
        '''Connect ALL the Buttons!!!'''


    
        


        
    def sendmsg(self, outMSG):
        encodedMSG = outMSG
        self.clntsock.send(encodedMSG.encode())

    def listen(self):

        self.boardgame.playerOneNameSlot.setText("Something")
        while True:
            try:
                incomingMSG = (self.clntsock.recv(1024).decode())
                print(incomingMSG, " received from ", self.ipaddress)
                
                if incomingMSG[0:4] == "Join":
                    self.setPlayers( incomingMSG )    
                if incomingMSG[0:4] == "Char":
                    self.setCharacters( incomingMSG )             


            except:
                print('Lost connection to server')
                self.clntsock.close()
                return False
        self.clntsock.close()

    def setCharacters(self, msg):

    	msg = msg[4:]
    	names = msg.split(',')
    
    	self.boardgame.scarlett.setEnabled(True)
    	self.boardgame.mustard.setEnabled(True)
    	self.boardgame.white.setEnabled(True)
    	self.boardgame.green.setEnabled(True)
    	self.boardgame.peacock.setEnabled(True)
    	self.boardgame.plum.setEnabled(True)
    
    	for name in msg:
    	    if name == "scarlett":
                self.boardgame.scarlett.setEnabled(False)
    	    elif name == "mustard":
                self.boardgame.mustard.setEnabled(False)
    	    elif name == "white":
                self.boardgame.white.setEnabled(False)
    	    elif name == "green":
                self.boardgame.green.setEnabled(False)
    	    elif name == "peacock":
                self.boardgame.peacock.setEnabled(False)
    	    elif name == "plum":
                self.boardgame.plum.setEnabled(False)

        
    def setPlayers(self, msg):
        
        msg = msg[4:]
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
    

    def clientmove(self, player, direction):
        encodeMSG = "1", player, direction
        sendmsg(encodeMSG)
        
    def clientsuggest(self, player, person, weapon, room):
        encodeMSG = "2", player, person, weapon, room
        sendmsg(encodeMSG)
        
    def clientaccuse(self, player, person, weapon, room):
        encodeMSG = "3", player, person, weapon, room
        sendmsg(encodeMSG)