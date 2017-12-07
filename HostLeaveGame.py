# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\HostLeaveGame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hostLeaveGame(object):
    def setupUi(self, hostLeaveGame):
        hostLeaveGame.setObjectName("hostLeaveGame")
        hostLeaveGame.resize(400, 300)
        self.hostLeaveButtonBox = QtWidgets.QDialogButtonBox(hostLeaveGame)
        self.hostLeaveButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.hostLeaveButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.hostLeaveButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.hostLeaveButtonBox.setCenterButtons(True)
        self.hostLeaveButtonBox.setObjectName("hostLeaveButtonBox")
        self.hLeavePart1 = QtWidgets.QLabel(hostLeaveGame)
        self.hLeavePart1.setGeometry(QtCore.QRect(50, 100, 301, 31))
        self.hLeavePart1.setAlignment(QtCore.Qt.AlignCenter)
        self.hLeavePart1.setObjectName("hLeavePart1")
        self.hLeavePart2 = QtWidgets.QLabel(hostLeaveGame)
        self.hLeavePart2.setGeometry(QtCore.QRect(50, 130, 301, 31))
        self.hLeavePart2.setAlignment(QtCore.Qt.AlignCenter)
        self.hLeavePart2.setObjectName("hLeavePart2")

        self.retranslateUi(hostLeaveGame)
        self.hostLeaveButtonBox.accepted.connect(hostLeaveGame.accept)
        self.hostLeaveButtonBox.rejected.connect(hostLeaveGame.reject)
        QtCore.QMetaObject.connectSlotsByName(hostLeaveGame)

    def retranslateUi(self, hostLeaveGame):
        _translate = QtCore.QCoreApplication.translate
        hostLeaveGame.setWindowTitle(_translate("hostLeaveGame", "Leave Game"))
        self.hLeavePart1.setText(_translate("hostLeaveGame", "Are you sure you want to leave the game?"))
        self.hLeavePart2.setText(_translate("hostLeaveGame", "Doing so will end the game."))

