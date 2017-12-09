# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\s03_SuggestionResponse.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuggestionShownDialog(object):
    def setupUi(self, SuggestionShownDialog):
        SuggestionShownDialog.setObjectName("SuggestionShownDialog")
        SuggestionShownDialog.resize(400, 300)
        self.SuggestionShownButtons = QtWidgets.QDialogButtonBox(SuggestionShownDialog)
        self.SuggestionShownButtons.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.SuggestionShownButtons.setOrientation(QtCore.Qt.Horizontal)
        self.SuggestionShownButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.SuggestionShownButtons.setCenterButtons(True)
        self.SuggestionShownButtons.setObjectName("SuggestionShownButtons")
        self.playerNameShowing = QtWidgets.QLabel(SuggestionShownDialog)
        self.playerNameShowing.setGeometry(QtCore.QRect(130, 30, 131, 31))
        self.playerNameShowing.setAlignment(QtCore.Qt.AlignCenter)
        self.playerNameShowing.setObjectName("playerNameShowing")
        self.suggestionActionLabel = QtWidgets.QLabel(SuggestionShownDialog)
        self.suggestionActionLabel.setGeometry(QtCore.QRect(50, 60, 301, 31))
        self.suggestionActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.suggestionActionLabel.setObjectName("suggestionActionLabel")
        self.cardShownLabel = QtWidgets.QLabel(SuggestionShownDialog)
        self.cardShownLabel.setGeometry(QtCore.QRect(170, 110, 61, 91))
        self.cardShownLabel.setAutoFillBackground(True)
        self.cardShownLabel.setText("")
        self.cardShownLabel.setPixmap(QtGui.QPixmap("leadPipeCard.jpg"))
        self.cardShownLabel.setScaledContents(True)
        self.cardShownLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cardShownLabel.setObjectName("cardShownLabel")

        self.retranslateUi(SuggestionShownDialog)
        self.SuggestionShownButtons.accepted.connect(SuggestionShownDialog.accept)
        self.SuggestionShownButtons.rejected.connect(SuggestionShownDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SuggestionShownDialog)

    def retranslateUi(self, SuggestionShownDialog):
        _translate = QtCore.QCoreApplication.translate
        SuggestionShownDialog.setWindowTitle(_translate("SuggestionShownDialog", "Suggestion Shown"))
        self.playerNameShowing.setText(_translate("SuggestionShownDialog", "TextLabel"))
        self.suggestionActionLabel.setText(_translate("SuggestionShownDialog", "has chosen to show you the following:"))

