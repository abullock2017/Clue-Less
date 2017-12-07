# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\s02_SuggestionAnnouncement.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuggestionMadeDialog(object):
    def setupUi(self, SuggestionMadeDialog):
        SuggestionMadeDialog.setObjectName("SuggestionMadeDialog")
        SuggestionMadeDialog.resize(400, 300)
        self.SuggestionMadeButtons = QtWidgets.QDialogButtonBox(SuggestionMadeDialog)
        self.SuggestionMadeButtons.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.SuggestionMadeButtons.setOrientation(QtCore.Qt.Horizontal)
        self.SuggestionMadeButtons.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.SuggestionMadeButtons.setCenterButtons(True)
        self.SuggestionMadeButtons.setObjectName("SuggestionMadeButtons")
        self.playerNameShowing = QtWidgets.QLabel(SuggestionMadeDialog)
        self.playerNameShowing.setGeometry(QtCore.QRect(130, 20, 131, 31))
        self.playerNameShowing.setAlignment(QtCore.Qt.AlignCenter)
        self.playerNameShowing.setObjectName("playerNameShowing")
        self.suggestionActionLabel = QtWidgets.QLabel(SuggestionMadeDialog)
        self.suggestionActionLabel.setGeometry(QtCore.QRect(50, 50, 301, 31))
        self.suggestionActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.suggestionActionLabel.setObjectName("suggestionActionLabel")
        self.cardShownLabel_3 = QtWidgets.QLabel(SuggestionMadeDialog)
        self.cardShownLabel_3.setGeometry(QtCore.QRect(270, 90, 61, 91))
        self.cardShownLabel_3.setAutoFillBackground(True)
        self.cardShownLabel_3.setText("")
        self.cardShownLabel_3.setPixmap(QtGui.QPixmap("loungeCard.jpg"))
        self.cardShownLabel_3.setScaledContents(True)
        self.cardShownLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.cardShownLabel_3.setObjectName("cardShownLabel_3")
        self.cardShownLabel = QtWidgets.QLabel(SuggestionMadeDialog)
        self.cardShownLabel.setGeometry(QtCore.QRect(70, 90, 61, 91))
        self.cardShownLabel.setAutoFillBackground(True)
        self.cardShownLabel.setText("")
        self.cardShownLabel.setPixmap(QtGui.QPixmap("peacock.jpg"))
        self.cardShownLabel.setScaledContents(True)
        self.cardShownLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cardShownLabel.setObjectName("cardShownLabel")
        self.cardShownLabel_2 = QtWidgets.QLabel(SuggestionMadeDialog)
        self.cardShownLabel_2.setGeometry(QtCore.QRect(170, 90, 61, 91))
        self.cardShownLabel_2.setAutoFillBackground(True)
        self.cardShownLabel_2.setText("")
        self.cardShownLabel_2.setPixmap(QtGui.QPixmap("leadPipeCard.jpg"))
        self.cardShownLabel_2.setScaledContents(True)
        self.cardShownLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cardShownLabel_2.setObjectName("cardShownLabel_2")
        self.label = QtWidgets.QLabel(SuggestionMadeDialog)
        self.label.setGeometry(QtCore.QRect(50, 190, 301, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(SuggestionMadeDialog)
        self.SuggestionMadeButtons.accepted.connect(SuggestionMadeDialog.accept)
        self.SuggestionMadeButtons.rejected.connect(SuggestionMadeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SuggestionMadeDialog)

    def retranslateUi(self, SuggestionMadeDialog):
        _translate = QtCore.QCoreApplication.translate
        SuggestionMadeDialog.setWindowTitle(_translate("SuggestionMadeDialog", "Suggestion Made"))
        self.playerNameShowing.setText(_translate("SuggestionMadeDialog", "TextLabel"))
        self.suggestionActionLabel.setText(_translate("SuggestionMadeDialog", "has made the following suggestion:"))
        self.label.setText(_translate("SuggestionMadeDialog", "Can you disprove this?"))

