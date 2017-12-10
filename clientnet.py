# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading
from PyQt5 import QtWidgets, QtMultimedia, QtCore, QtGui
from PyQt5.QtWidgets import *
from GameBoard import Ui_GameBoard
from ClueLess import Ui_ClueLess as MainMenu
from s01_SuggestionDialog import Ui_SuggestionDialog as Suggestion
from s02_SuggestionAnnouncement import Ui_SuggestionMadeDialog as SuggestionAnnouncement
from a01_AccusationDialog import Ui_AccusationDialog as Accusation
from a03a_AccusationWinner import Ui_WinnerDialog as Winner
from a03b_AccusationLoser import Ui_YouLoseDialog as Loser
from GameOptions import Ui_GameOptions as GameOptions
from HostLeaveGame import Ui_hostLeaveGame as HostLeave
from PlayerLeaveGame import Ui_playerLeaveGame as PlayerLeave
from EmptySuggestionResponse import Ui_emptySuggestionResponse as EmptyResponse
from s03_SuggestionResponse import Ui_SuggestionShownDialog as SuggestionResponse
from EndTurnDialog import Ui_endTurnWindow as EndTurn
from m01_YourTurnDialog import Ui_YourTurnDialog as YourTurn

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
        msg = self.playerNumber + "Char" + character
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
        self.boardgame.makeSuggestionButton.clicked.connect(self.makeSuggestion)
        self.boardgame.leaveGameButton.clicked.connect(self.leaveGameMSG)
        self.boardgame.inGameOptionsButton.clicked.connect(self.options)
        self.boardgame.makeAccusationButton.clicked.connect(self.makeAccusation)

    def endTurnMSG(self):
        msg = 'End'
        self.sendmsg(msg)
    
    def options(self):
        self.mainMenu = QtWidgets.QDialog()
        self.mainMenu.ui = MainMenu()
        self.mainMenu.ui.setupUi(self.mainMenu)
        self.gameOptions = QtWidgets.QDialog()
        self.gameOptions.ui = GameOptions()
        self.gameOptions.ui.setupUi(self.gameOptions)
        self.gameOptions.ui.horizontalSlider.setValue(self.mainMenu.ui.mainMusicSlider.value())
        self.gameOptions.show()
        self.gameOptions.ui.horizontalSlider.valueChanged[int].connect(self.changeVolume)
        

    def changeVolume(self):
        self.mainMenu.musicPlayer.setVolume(self.ui.mainMusicSlider.value())
        self.gameOptions.ui.horizontalSlider.setValue(self.mainMenu.ui.mainMusicSlider.value())

    def leaveGameMSG(self, playerType):
        msg = "Leave" + playerType + "," + '''player number?'''
        self.sendmsg(msg)

    def makeAccusationMSG(self, character, weapon, room):
        msg = "Accuse" + character + "," + weapon + "," + room
        self.sendmsg(msg)

    def makeSuggestionMSG(self, character, weapon, room):
        msg = "Suggest" + character + "," + weapon + "," + room
        self.sendmsg(msg)
        
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
                if incomingMSG[0:8] == "Disprove":
                    self.displaySuggestionAnnouncement(incomingMSG)
                if incomingMSG[0:6] == "Result":
                    self.displayAccusationResult(incomingMSG)
                if incomingMSG[0:3] == "End":
                    self.displayEndTurn()
                if incomingMSG[0:4] == "Turn":
                    self.displayYourTurn(incomingMSG)
                if incomingMSG[0:5] == "Leave":
                    self.leaveGame(incomingMSG)
                if incomingMSG[0:8] == "Response":
                    self.displaySuggestionResponse(incomingMSG)

            except:
                print('Lost connection to server')
                self.clntsock.close()
                return False
        self.clntsock.close()

    def displayEndTurn(self):
        self.endTurn = QtWidgets.QDialog()
        self.endTurn.ui = EndTurn()
        self.endTurn.ui.setupUi(self.endTurn)
        self.endTurn.show()
        self.endTurn.ui.endTurnButton.clicked.connect(self.endTurnMSG())
        self.endTurn.ui.finalAccusationButton.clicked.connect(self.makeAccusation()())
        
    def makeAccusation(self):
        self.accusation = QtWidgets.QDialog()
        self.accusation.ui = Accusation()
        self.accusation.ui.setupUi(self.accusation)
        self.accusation.show()
        self.accusation.ui.accusationButtonBox.accepted.connect(lambda: self.makeAccusationMSG(self.accusation.ui.characterAccusation.currentText(),
                                                                                                           self.accusation.ui.weaponAccusation.currentText(), 
                                                                                                           self.accusation.ui.roomAccusation.currentText()))
    
    def displayAccusationResult(self, incomingMSG):
        self.winner = QtWidgets.QDialog()
        self.winner.ui = Winner()
        self.winner.ui.setupUi(self.winner)
        self.loser = QtWidgets.QDialog()
        self.loser.ui = Loser()
        self.loser.ui.setupUi(self.loser)
        msg = incomingMSG[6:]
        results = msg.split(",")
        if (results[0] == "win"):
            self.winner.ui.finalCharacter.setPixmap(QtGui.QPixmap(self.setCardImage(results[1])))
            self.winner.ui.finalWeapon.setPixmap(QtGui.QPixmap(self.setCardImage(results[2])))
            self.winner.ui.finalRoom.setPixmap(QtGui.QPixmap(self.setCardImage(results[3])))
            self.winner.show()
        else:
            self.loser.show()

    def displayYourTurn(self):
        self.turn = QtWidgets.QDialog()
        self.turn.ui = YourTurn()
        self.turn.ui.setupUi(self.turn)
        self.turn.show()

    def makeSuggestion(self):
        self.suggestion = QtWidgets.QDialog()
        self.suggestion.ui = Suggestion()
        self.suggestion.ui.setupUi(self.suggestion)
        '''This is where we search the list of options based on what room the player is currently in'''
        index = self.suggestion.ui.roomSuggestion.findText("Billiard Room", QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.suggestion.ui.roomSuggestion.setCurrentIndex(index)
        self.suggestion.show()
        self.suggestion.ui.suggestionButtonBox.accepted.connect(lambda: self.makeSuggestionMSG(self.suggestion.ui.characterSuggestion.currentText(),
                                                                                                           self.suggestion.ui.weaponSuggestion.currentText(), 
                                                                                                           self.suggestion.ui.roomSuggestion.currentText()))
        
    def displaySuggestionAnnouncement(self, incomingMSG):
        msg = incomingMSG[8:]
        suggestions = msg.split(",")
        self.suggestionAnnouncement = QtWidgets.QDialog()
        self.suggestionAnnouncement.ui = SuggestionAnnouncement()
        self.suggestionAnnouncement.ui.setupUi(self.suggestionAnnouncement)
        self.suggestionAnnouncement.ui.cardShownLabel.setPixmap(QtGui.QPixmap(self.setCardImage(suggestions[0])))
        self.suggestionAnnouncement.ui.cardShownLabel_2.setPixmap(QtGui.QPixmap(self.setCardImage(suggestions[1])))
        self.suggestionAnnouncement.ui.cardShownLabel_3.setPixmap(QtGui.QPixmap(self.setCardImage(suggestions[2])))
        self.suggestionAnnouncement.show()

    def displaySuggestionResponse(self, incomingMSG):
        msg = incomingMSG[8:]
        responseInfo = msg.split(',')
        self.suggestionResponse = QtWidgets.QDialog()
        self.suggestionResponse.ui = SuggestionResponse()
        self.suggestionResponse.ui.setupUi(self.suggestionResponse)
        self.emptyResponse = QtWidgets.QDialog()
        self.emptyResponse.ui = EmptyResponse()
        self.emptyResponse.ui.setupUi(self.emptyResponse)
        if (responseInfo[0] == "empty"):
            self.emptyResponse.show()
        else:
            self.suggestionResponse.ui.cardShownLabel.setPixmap(QtGui.QPixmap(self.setCardImage(responseInfo[1])))
            self.suggestionResponse.show()

    def setCardImage(self, cardValue):
        if (cardValue.lower() == "miss scarlet"):
            return "scarlett.jpg"
        elif (cardValue.lower() == "colonel mustard"):
            return "mustard.jpg"
        elif (cardValue.lower() == "mrs. white"):
            return "white.jpg"
        elif (cardValue.lower() == "mr. green"):
            return "green.jpg"
        elif (cardValue.lower() == "mrs. peacock"):
            return "peacock.jpg"
        elif (cardValue.lower() == "professor plum"):
            return "plum.jpg"
        elif (cardValue.lower() == "candlestick"):
            return "candlestickCard.jpg"
        elif (cardValue.lower() == "revolver"):
            return "revolverCard.jpg"
        elif (cardValue.lower() == "wrench"):
            return "wrenchCard.png"
        elif (cardValue.lower() == "rope"):
            return "ropeCard.png"
        elif (cardValue.lower() == "knife"):
            return "knifeCard.jpg"
        elif (cardValue.lower() == "lead pipe"):
            return "leadPipeCard.jpg"
        elif (cardValue.lower() == "conservatory"):
            return "conservatoryCard.jpg"
        elif (cardValue.lower() == "study"):
            return "studyCard.jpg"
        elif (cardValue.lower() == "billiard room"):
            return "billiardRoomCard.jpg"
        elif (cardValue.lower() == "dining room"):
            return "diningRoomCard.jpg"
        elif (cardValue.lower() == "kitchen"):
            return "kitchenCard.jpg"
        elif (cardValue.lower() == "library"):
            return "libraryCard.jpg"
        elif (cardValue.lower() == "hall"):
            return "hallCard.jpg"
        elif (cardValue.lower() == "lounge"):
            return "loungeCard.jpg"
        else:
            return "ballroomCard.jpg"

    def leaveGame(self, incomingmsg):
        msg = incomingmsg[5:]
        
        self.hostLeave = QtWidgets.QDialog()
        self.hostLeave.ui = HostLeave()
        self.hostLeave.ui.setupUi(self.hostLeave)
        self.playerLeave = QtWidgets.QDialog()
        self.playerLeave.ui = PlayerLeave()
        self.playerLeave.ui.setupUi(self.playerLeave)
        
        if (msg == "host"):
            self.hostLeave.show()
            self.hostLeave.ui.hostLeaveButtonBox.accepted.connect(self.closeEvent())
            ''' Or do we want to send message to server to cut connection? '''
        else:
            self.playerLeave.show()
            ''' Send message back to server to send all clients player lost message '''
            ''' Send message to server to remove player from game? '''
        
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