# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\PlayerLeaveGame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_playerLeaveGame(object):
    def setupUi(self, playerLeaveGame):
        playerLeaveGame.setObjectName("playerLeaveGame")
        playerLeaveGame.resize(400, 300)
        self.playerLeaveButtonBox = QtWidgets.QDialogButtonBox(playerLeaveGame)
        self.playerLeaveButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.playerLeaveButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.playerLeaveButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.playerLeaveButtonBox.setCenterButtons(True)
        self.playerLeaveButtonBox.setObjectName("playerLeaveButtonBox")
        self.pLeavePart1 = QtWidgets.QLabel(playerLeaveGame)
        self.pLeavePart1.setGeometry(QtCore.QRect(50, 100, 301, 31))
        self.pLeavePart1.setAlignment(QtCore.Qt.AlignCenter)
        self.pLeavePart1.setObjectName("pLeavePart1")
        self.pLeavePart2 = QtWidgets.QLabel(playerLeaveGame)
        self.pLeavePart2.setGeometry(QtCore.QRect(50, 130, 301, 31))
        self.pLeavePart2.setAlignment(QtCore.Qt.AlignCenter)
        self.pLeavePart2.setObjectName("pLeavePart2")

        self.retranslateUi(playerLeaveGame)
        self.playerLeaveButtonBox.accepted.connect(playerLeaveGame.accept)
        self.playerLeaveButtonBox.rejected.connect(playerLeaveGame.reject)
        QtCore.QMetaObject.connectSlotsByName(playerLeaveGame)

    def retranslateUi(self, playerLeaveGame):
        _translate = QtCore.QCoreApplication.translate
        playerLeaveGame.setWindowTitle(_translate("playerLeaveGame", "Leave Game"))
        self.pLeavePart1.setText(_translate("playerLeaveGame", "Are you sure you want to leave the game?"))
        self.pLeavePart2.setText(_translate("playerLeaveGame", "You will not be able to rejoin."))

