# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\a03a_AccusationWinner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WinnerDialog(object):
    def setupUi(self, WinnerDialog):
        WinnerDialog.setObjectName("WinnerDialog")
        WinnerDialog.resize(400, 300)
        self.WinnerButtons = QtWidgets.QDialogButtonBox(WinnerDialog)
        self.WinnerButtons.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.WinnerButtons.setOrientation(QtCore.Qt.Horizontal)
        self.WinnerButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.WinnerButtons.setCenterButtons(True)
        self.WinnerButtons.setObjectName("WinnerButtons")
        self.finalCharacter = QtWidgets.QLabel(WinnerDialog)
        self.finalCharacter.setGeometry(QtCore.QRect(70, 120, 61, 91))
        self.finalCharacter.setAutoFillBackground(True)
        self.finalCharacter.setText("")
        self.finalCharacter.setPixmap(QtGui.QPixmap("peacock.jpg"))
        self.finalCharacter.setScaledContents(True)
        self.finalCharacter.setAlignment(QtCore.Qt.AlignCenter)
        self.finalCharacter.setObjectName("finalCharacter")
        self.finalWeapon = QtWidgets.QLabel(WinnerDialog)
        self.finalWeapon.setGeometry(QtCore.QRect(170, 120, 61, 91))
        self.finalWeapon.setAutoFillBackground(True)
        self.finalWeapon.setText("")
        self.finalWeapon.setPixmap(QtGui.QPixmap("leadPipeCard.jpg"))
        self.finalWeapon.setScaledContents(True)
        self.finalWeapon.setAlignment(QtCore.Qt.AlignCenter)
        self.finalWeapon.setObjectName("finalWeapon")
        self.finalRoom = QtWidgets.QLabel(WinnerDialog)
        self.finalRoom.setGeometry(QtCore.QRect(270, 120, 61, 91))
        self.finalRoom.setAutoFillBackground(True)
        self.finalRoom.setText("")
        self.finalRoom.setPixmap(QtGui.QPixmap("loungeCard.jpg"))
        self.finalRoom.setScaledContents(True)
        self.finalRoom.setAlignment(QtCore.Qt.AlignCenter)
        self.finalRoom.setObjectName("finalRoom")
        self.winnerName = QtWidgets.QLabel(WinnerDialog)
        self.winnerName.setGeometry(QtCore.QRect(130, 30, 131, 31))
        self.winnerName.setAlignment(QtCore.Qt.AlignCenter)
        self.winnerName.setObjectName("winnerName")
        self.winActionLabel = QtWidgets.QLabel(WinnerDialog)
        self.winActionLabel.setGeometry(QtCore.QRect(50, 60, 301, 31))
        self.winActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.winActionLabel.setObjectName("winActionLabel")

        self.retranslateUi(WinnerDialog)
        self.WinnerButtons.accepted.connect(WinnerDialog.accept)
        self.WinnerButtons.rejected.connect(WinnerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WinnerDialog)

    def retranslateUi(self, WinnerDialog):
        _translate = QtCore.QCoreApplication.translate
        WinnerDialog.setWindowTitle(_translate("WinnerDialog", "Winner!"))
        self.winnerName.setText(_translate("WinnerDialog", "TextLabel"))
        self.winActionLabel.setText(_translate("WinnerDialog", "has won the game with the following:"))

