# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\EndTurnDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_endTurnWindow(object):
    def setupUi(self, endTurnWindow):
        endTurnWindow.setObjectName("endTurnWindow")
        endTurnWindow.resize(400, 300)
        endTurnWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.endTurnButton = QtWidgets.QPushButton(endTurnWindow)
        self.endTurnButton.setGeometry(QtCore.QRect(110, 60, 191, 41))
        self.endTurnButton.setObjectName("endTurnButton")
        self.finalAccusationButton = QtWidgets.QPushButton(endTurnWindow)
        self.finalAccusationButton.setGeometry(QtCore.QRect(110, 200, 191, 41))
        self.finalAccusationButton.setObjectName("finalAccusationButton")
        self.finalAccusationWarningLbel = QtWidgets.QLabel(endTurnWindow)
        self.finalAccusationWarningLbel.setGeometry(QtCore.QRect(84, 120, 241, 61))
        self.finalAccusationWarningLbel.setAlignment(QtCore.Qt.AlignCenter)
        self.finalAccusationWarningLbel.setWordWrap(True)
        self.finalAccusationWarningLbel.setObjectName("finalAccusationWarningLbel")

        self.retranslateUi(endTurnWindow)
        QtCore.QMetaObject.connectSlotsByName(endTurnWindow)

    def retranslateUi(self, endTurnWindow):
        _translate = QtCore.QCoreApplication.translate
        endTurnWindow.setWindowTitle(_translate("endTurnWindow", "End Turn?"))
        self.endTurnButton.setText(_translate("endTurnWindow", "End Turn"))
        self.finalAccusationButton.setText(_translate("endTurnWindow", "Final Accusation"))
        self.finalAccusationWarningLbel.setText(_translate("endTurnWindow", "Remember, if you make your final accusation and you are wrong, you lose."))

