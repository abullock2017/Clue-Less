'''
Created on Nov 5, 2017

@author: abull
'''

import sys
import socket
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from ClueLess import Ui_ClueLess

'''
from mainMenuWindow import Ui_MainMenuWindow
from gameLobbyMenuWindow import Ui_GameLobbyWindow
from mainOptionsMenuWindow import Ui_MainOptionsMenuWindow
'''

class Main(QWidget, Ui_ClueLess):
    
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_ClueLess()
        self.ui.setupUi(self)
        '''self.ui.stackedWidget.setCurrentIndex(0)'''
        self.ui.mainMusicSlider.valueChanged[int].connect(self.changeVolume)
        self.ui.gameLobbyButton.clicked.connect(self.displayGameLobbyMenu)
        self.ui.mainOptionsButton.clicked.connect(self.mainOptionsButton_Clicked)
    
    def changeVolume(self, value):
        musicPlayer.setVolume(value)
    
    def goBack(self, hideMenu, showMenu):
        hideMenu.hide()
        showMenu.show()
    
    def displayGameLobbyMenu(self):
        self.ui.mainMenu.hide()
        self.ui.gameLobbyMenu.show()
        self.ui.createGameButton.clicked.connect(self.displayCreateGameMenu)
        self.ui.joinGameButton.clicked.connect(self.displayJoinGameMenu)
        self.ui.gameLobbyBack.clicked.connect(lambda: self.goBack(self.ui.gameLobbyMenu, self.ui.mainMenu))
       
    def displayCreateGameMenu(self):
        self.ui.gameLobbyMenu.hide()
        self.ui.createGameMenu.show()
        hostName = socket.gethostname()
        ipAddress = socket.gethostbyname(hostName)
        self.ui.ipAddressLabel.setText(ipAddress)
        self.ui.createButton.clicked.connect(lambda: self.displayGameLobby("gameHost"))
        self.ui.cancelButton.clicked.connect(lambda: self.goBack(self.ui.createGameMenu, self.ui.gameLobbyMenu))
        
    def displayJoinGameMenu(self):
        self.ui.gameLobbyMenu.hide()
        self.ui.joinGameMenu.show()
        self.ui.joinGameButton_3.clicked.connect(lambda: self.displayGameLobby("newPlayer"))
        self.ui.cancelJoinButton.clicked.connect(lambda: self.goBack(self.ui.joinGameMenu, self.ui.gameLobbyMenu))
        
    def displayGameLobby(self, playerType):
        if playerType == "gameHost":
            self.ui.playerOneNameSlot.setText(self.ui.gameHostName.text())
        else:
            if self.ui.playerTwoNameSlot.text() == "Waiting...":
                self.ui.playerTwoNameSlot.setText(self.ui.newPlayerName.text())
            elif self.ui.playerThreeNameSlot.text() == "Waiting...":
                self.ui.playerThreeNameSlot.setText(self.ui.newPlayerName.text())
            elif self.ui.playerFourNameSlot.text() == "Waiting...":
                self.ui.playerFourNameSlot.setText(self.ui.newPlayerName.text())
            elif self.ui.playerFiveNameSlot.text() == "Waiting...":
                self.ui.playerFiveNameSlot.setText(self.ui.newPlayerName.text())
            elif self.ui.playerSixNameSlot.text() == "Waiting...":
                self.ui.playerSixNameSlot.setText(self.ui.newPlayerName.text())
            else:
                '''Display some message, the game is full'''
        if self.ui.playerThreeNameSlot != "Waiting...":
            self.ui.startGameButton.setEnabled(True)
        if playerType == "gameHost":
            self.ui.createGameMenu.hide()
        else:
            self.ui.joinGameMenu.hide()
        self.ui.gameLobby.show()
        self.ui.startGameButton.clicked.connect(self.displayCharacterSelection)
        self.ui.cancelStartButton.clicked.connect(lambda: self.goBack(self.ui.gameLobby, self.ui.gameLobbyMenu))
    
    def displayCharacterSelection(self):
        self.ui.gameLobby.hide()
        self.ui.characterSelection.show()
    
    def mainOptionsButton_Clicked(self):
        self.ui.mainMenu.hide()
        self.ui.mainOptionsMenu.show()
        self.ui.mainOptionsBack.clicked.connect(lambda: self.goBack(self.ui.mainOptionsMenu, self.ui.mainMenu))
       
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    musicPlayer = QtMultimedia.QMediaPlayer()
    musicSound = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("D:\Downloads\clue_music.wma"))
    musicPlayer.setMedia(musicSound)
    musicPlayer.setVolume(100)
    window = Main()
    window.show()
    musicPlayer.play()
    sys.exit(app.exec_())