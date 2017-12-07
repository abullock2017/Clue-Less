'''
Created on Nov 5, 2017

@author: abull
'''

import sys
import socket
import ipgetter
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from ClueLess import Ui_ClueLess
from GameBoard import Ui_GameBoard
from SuggestionDialog import Ui_SuggestionDialog
import webbrowser

from _thread import *
import threading
from servernet import ServerNet
from clientnet import ClientNet

port = 12346

class Main(QWidget, Ui_ClueLess, Ui_GameBoard):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ClueLess()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.mainMusicSlider.valueChanged[int].connect(self.changeVolume)
        self.ui.gameLobbyButton.clicked.connect(self.displayGameLobbyMenu)
        self.ui.mainOptionsButton.clicked.connect(self.mainOptionsButton_Clicked)
        self.ui.instructionsButton.clicked.connect(self.howToPlay)
		
    def howToPlay(self):
        webbrowser.open('https://www.hasbro.com/common/documents/dad2885d1c4311ddbd0b0800200c9a66/2BFAEC9E5056900B102C3859E9AC6332.pdf')
    
    def changeVolume(self):
        musicPlayer.setVolume(self.ui.mainMusicSlider.value())
    
    def goBack(self, hideMenu, showMenu):
        hideMenu.hide()
        showMenu.show()
    
    def displayGameLobbyMenu(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.mainMenu.hide()
        self.ui.gameLobbyMenu.show()
        self.ui.createGameButton.clicked.connect(self.displayCreateGameMenu)
        self.ui.joinGameButton.clicked.connect(self.displayJoinGameMenu)
        self.ui.gameLobbyBack.clicked.connect(lambda: self.goBack(self.ui.gameLobbyMenu, self.ui.mainMenu))
       
    def displayCreateGameMenu(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.gameLobbyMenu.hide()
        self.ui.createGameMenu.show()
        ipAddress = ipgetter.myip()
        self.ui.ipAddressLabel.setText(ipAddress)
        self.ui.createButton.clicked.connect(lambda: self.displayGameLobby("gameHost"))
        self.ui.cancelButton.clicked.connect(lambda: self.goBack(self.ui.createGameMenu, self.ui.gameLobbyMenu))
        
    def displayJoinGameMenu(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.gameLobbyMenu.hide()
        self.ui.joinGameMenu.show()
        self.ui.joinGameButton_3.clicked.connect(lambda: self.displayGameLobby("newPlayer"))
        self.ui.cancelJoinButton.clicked.connect(lambda: self.goBack(self.ui.joinGameMenu, self.ui.gameLobbyMenu))
        
    def displayGameLobby(self, playerType):
        
        if playerType == "gameHost":
            startsocket = ServerNet(port, self.ui.gameHostName.text()) #Instantiate server class
            threading.Thread(target = startsocket.listen).start() # Server is now listening
            startsocket.show()
			
        else:
            self.playertype = "newPlayer"
            host = self.ui.gameIPInput.text()
            clientconnection = ClientNet(host, self.ui.newPlayerName.text()) #Established socket to server
            clientconnection.show()
            print("client created")
            
        if playerType == "gameHost":
            self.ui.createGameMenu.hide()
        else:
            self.ui.joinGameMenu.hide()

        
    def displayGameBoard(self):
        self.ui.characterSelection.hide()
        
    
    def mainOptionsButton_Clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.mainMenu.hide()
        self.ui.mainOptionsMenu.show()
        self.ui.mainOptionsBack.clicked.connect(lambda: self.goBack(self.ui.mainOptionsMenu, self.ui.mainMenu))
        
		
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    musicPlayer = QtMultimedia.QMediaPlayer()
    musicSound = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("clue_music.wma"))
    musicPlayer.setMedia(musicSound)
    musicPlayer.setVolume(100)
    musicPlayer.play()
    window = Main()
    window.show()
    sys.exit(app.exec_())