# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\SuggestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuggestionDialog(object):
    def setupUi(self, SuggestionDialog):
        SuggestionDialog.setObjectName("SuggestionDialog")
        SuggestionDialog.resize(400, 300)
        self.suggestionButtonBox = QtWidgets.QDialogButtonBox(SuggestionDialog)
        self.suggestionButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.suggestionButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.suggestionButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.suggestionButtonBox.setCenterButtons(True)
        self.suggestionButtonBox.setObjectName("suggestionButtonBox")
        self.characterSuggestion = QtWidgets.QComboBox(SuggestionDialog)
        self.characterSuggestion.setGeometry(QtCore.QRect(70, 60, 261, 31))
        self.characterSuggestion.setObjectName("characterSuggestion")
        self.characterSuggestion.addItem("")
        self.characterSuggestion.addItem("")
        self.characterSuggestion.addItem("")
        self.characterSuggestion.addItem("")
        self.characterSuggestion.addItem("")
        self.characterSuggestion.addItem("")
        self.characterSuggestion.addItem("")
        self.weaponSuggestion = QtWidgets.QComboBox(SuggestionDialog)
        self.weaponSuggestion.setGeometry(QtCore.QRect(70, 120, 261, 31))
        self.weaponSuggestion.setObjectName("weaponSuggestion")
        self.weaponSuggestion.addItem("")
        self.weaponSuggestion.addItem("")
        self.weaponSuggestion.addItem("")
        self.weaponSuggestion.addItem("")
        self.weaponSuggestion.addItem("")
        self.weaponSuggestion.addItem("")
        self.weaponSuggestion.addItem("")
        self.roomSuggestion = QtWidgets.QComboBox(SuggestionDialog)
        self.roomSuggestion.setGeometry(QtCore.QRect(70, 180, 261, 31))
        self.roomSuggestion.setObjectName("roomSuggestion")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")
        self.roomSuggestion.addItem("")

        self.retranslateUi(SuggestionDialog)
        self.suggestionButtonBox.accepted.connect(SuggestionDialog.accept)
        self.suggestionButtonBox.rejected.connect(SuggestionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SuggestionDialog)

    def retranslateUi(self, SuggestionDialog):
        _translate = QtCore.QCoreApplication.translate
        SuggestionDialog.setWindowTitle(_translate("SuggestionDialog", "Make a Suggestion"))
        self.characterSuggestion.setItemText(0, _translate("SuggestionDialog", "Select a Character..."))
        self.characterSuggestion.setItemText(1, _translate("SuggestionDialog", "Mrs. White"))
        self.characterSuggestion.setItemText(2, _translate("SuggestionDialog", "Miss Scarlet"))
        self.characterSuggestion.setItemText(3, _translate("SuggestionDialog", "Colonel Mustard"))
        self.characterSuggestion.setItemText(4, _translate("SuggestionDialog", "Professor Plum"))
        self.characterSuggestion.setItemText(5, _translate("SuggestionDialog", "Mrs. Peacock"))
        self.characterSuggestion.setItemText(6, _translate("SuggestionDialog", "Mr. Green"))
        self.weaponSuggestion.setItemText(0, _translate("SuggestionDialog", "Select a Weapon..."))
        self.weaponSuggestion.setItemText(1, _translate("SuggestionDialog", "Candlestick"))
        self.weaponSuggestion.setItemText(2, _translate("SuggestionDialog", "Revolver"))
        self.weaponSuggestion.setItemText(3, _translate("SuggestionDialog", "Wrench"))
        self.weaponSuggestion.setItemText(4, _translate("SuggestionDialog", "Rope"))
        self.weaponSuggestion.setItemText(5, _translate("SuggestionDialog", "Knife"))
        self.weaponSuggestion.setItemText(6, _translate("SuggestionDialog", "Lead Pipe"))
        self.roomSuggestion.setItemText(0, _translate("SuggestionDialog", "Select a Room..."))
        self.roomSuggestion.setItemText(1, _translate("SuggestionDialog", "Conservatory"))
        self.roomSuggestion.setItemText(2, _translate("SuggestionDialog", "Study"))
        self.roomSuggestion.setItemText(3, _translate("SuggestionDialog", "Billiard Room"))
        self.roomSuggestion.setItemText(4, _translate("SuggestionDialog", "Dining Room"))
        self.roomSuggestion.setItemText(5, _translate("SuggestionDialog", "Kitchen"))
        self.roomSuggestion.setItemText(6, _translate("SuggestionDialog", "Library"))
        self.roomSuggestion.setItemText(7, _translate("SuggestionDialog", "Hall"))
        self.roomSuggestion.setItemText(8, _translate("SuggestionDialog", "Lounge"))
        self.roomSuggestion.setItemText(9, _translate("SuggestionDialog", "Ballroom"))

