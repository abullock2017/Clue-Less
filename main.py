'''
Created on Nov 5, 2017

@author: abull
'''

import sys
import socket
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from ClueLess import Ui_ClueLess
import webbrowser

from _thread import *
import threading
from servernet import ServerNet
from clientnet import ClientNet

port = 12346

'''
from mainMenuWindow import Ui_MainMenuWindow
from gameLobbyMenuWindow import Ui_GameLobbyWindow
from mainOptionsMenuWindow import Ui_MainOptionsMenuWindow
'''

class Main(QWidget, Ui_ClueLess):
    
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
        musicPlayer.setVolume( self.ui.mainMusicSlider.value() )
    
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
        hostName = socket.gethostname()
        ipAddress = socket.gethostbyname(hostName)
        self.ui.ipAddressLabel.setText(ipAddress)
        self.ui.createButton.clicked.connect(lambda: self.displayGameLobby("gameHost"))
        self.ui.cancelButton.clicked.connect(lambda: self.goBack(self.ui.createGameMenu, self.ui.gameLobbyMenu))
        
    def displayJoinGameMenu(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.gameLobbyMenu.hide()
        self.ui.joinGameMenu.show()
        self.ui.joinGameButton_3.clicked.connect(lambda: self.displayGameLobby("newPlayer"))
        self.ui.cancelJoinButton.clicked.connect(lambda: self.goBack(self.ui.joinGameMenu, self.ui.gameLobbyMenu))
        
    def displayGameLobby(self, playerType):
        
        self.ui.playerThreeNameSlot.setText( "Person" )
        
        if playerType == "gameHost":
            self.ui.playerOneNameSlot.setText(self.ui.gameHostName.text())
            
            startsocket = ServerNet(port)   #Instantiate server class
            threading.Thread(target = startsocket.listen).start() #Server is now listening for connection requests
            print("server created")
            
            '''
            while True:
                massmsg = input("MSG to all clients: ")   # Need to verify valid IP address?
                startsocket.sendmsgtoclients(massmsg)
            '''
            
        else:
            
            
            #host = input("Please enter IP address: ")   #This get server IP from user
            host = self.ui.gameIPInput.text()
            clientconnection = ClientNet(host)          #Established socket to server
            print("client created")
            clientconnection.sendmsg("hello")
            
            '''
            while True:
                message = input("Please enter message to server: ")
                if  (message == 'end'):
                    break
                clientconnection.sendmsg(message)
            '''
            
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
        if self.ui.playerThreeNameSlot.text() != "Waiting...":
            self.ui.startGameButton.setEnabled(True)
        if playerType == "gameHost":
            self.ui.createGameMenu.hide()
        else:
            self.ui.joinGameMenu.hide()
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.gameLobby.show()
        self.ui.startGameButton.clicked.connect(self.displayCharacterSelection)
        self.ui.cancelStartButton.clicked.connect(lambda: self.goBack(self.ui.gameLobby, self.ui.gameLobbyMenu))
    
    def displayCharacterSelection(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.gameLobby.hide()
        self.ui.characterSelection.show()
        self.ui.continueButton.clicked.connect(self.displayGameBoard)
    
    def displayGameBoard(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.characterSelection.hide()
        self.ui.gameBoard.show()
    
    def mainOptionsButton_Clicked(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        self.ui.mainMenu.hide()
        self.ui.mainOptionsMenu.show()
        self.ui.mainOptionsBack.clicked.connect(lambda: self.goBack(self.ui.mainOptionsMenu, self.ui.mainMenu))
       
    def closeEvent(self, *args, **kwargs):
        startsocket.terminate()
        clientconnection.terminate()
        return QWidget.closeEvent(self, *args, **kwargs)
    
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