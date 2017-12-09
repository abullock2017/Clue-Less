# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\a01_AccusationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccusationDialog(object):
    def setupUi(self, AccusationDialog):
        AccusationDialog.setObjectName("AccusationDialog")
        AccusationDialog.resize(400, 300)
        self.accusationButtonBox = QtWidgets.QDialogButtonBox(AccusationDialog)
        self.accusationButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.accusationButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.accusationButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.accusationButtonBox.setCenterButtons(True)
        self.accusationButtonBox.setObjectName("accusationButtonBox")
        self.characterAccusation = QtWidgets.QComboBox(AccusationDialog)
        self.characterAccusation.setGeometry(QtCore.QRect(70, 60, 261, 31))
        self.characterAccusation.setObjectName("characterAccusation")
        self.characterAccusation.addItem("")
        self.characterAccusation.addItem("")
        self.characterAccusation.addItem("")
        self.characterAccusation.addItem("")
        self.characterAccusation.addItem("")
        self.characterAccusation.addItem("")
        self.characterAccusation.addItem("")
        self.weaponAccusation = QtWidgets.QComboBox(AccusationDialog)
        self.weaponAccusation.setGeometry(QtCore.QRect(70, 120, 261, 31))
        self.weaponAccusation.setObjectName("weaponAccusation")
        self.weaponAccusation.addItem("")
        self.weaponAccusation.addItem("")
        self.weaponAccusation.addItem("")
        self.weaponAccusation.addItem("")
        self.weaponAccusation.addItem("")
        self.weaponAccusation.addItem("")
        self.weaponAccusation.addItem("")
        self.roomAccusation = QtWidgets.QComboBox(AccusationDialog)
        self.roomAccusation.setGeometry(QtCore.QRect(70, 180, 261, 31))
        self.roomAccusation.setObjectName("roomAccusation")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")
        self.roomAccusation.addItem("")

        self.retranslateUi(AccusationDialog)
        self.accusationButtonBox.accepted.connect(AccusationDialog.accept)
        self.accusationButtonBox.rejected.connect(AccusationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccusationDialog)

    def retranslateUi(self, AccusationDialog):
        _translate = QtCore.QCoreApplication.translate
        AccusationDialog.setWindowTitle(_translate("AccusationDialog", "Make an Accusation"))
        self.characterAccusation.setItemText(0, _translate("AccusationDialog", "Select a Character..."))
        self.characterAccusation.setItemText(1, _translate("AccusationDialog", "Mrs. White"))
        self.characterAccusation.setItemText(2, _translate("AccusationDialog", "Miss Scarlet"))
        self.characterAccusation.setItemText(3, _translate("AccusationDialog", "Colonel Mustard"))
        self.characterAccusation.setItemText(4, _translate("AccusationDialog", "Professor Plum"))
        self.characterAccusation.setItemText(5, _translate("AccusationDialog", "Mrs. Peacock"))
        self.characterAccusation.setItemText(6, _translate("AccusationDialog", "Mr. Green"))
        self.weaponAccusation.setItemText(0, _translate("AccusationDialog", "Select a Weapon..."))
        self.weaponAccusation.setItemText(1, _translate("AccusationDialog", "Candlestick"))
        self.weaponAccusation.setItemText(2, _translate("AccusationDialog", "Revolver"))
        self.weaponAccusation.setItemText(3, _translate("AccusationDialog", "Wrench"))
        self.weaponAccusation.setItemText(4, _translate("AccusationDialog", "Rope"))
        self.weaponAccusation.setItemText(5, _translate("AccusationDialog", "Knife"))
        self.weaponAccusation.setItemText(6, _translate("AccusationDialog", "Lead Pipe"))
        self.roomAccusation.setItemText(0, _translate("AccusationDialog", "Select a Room..."))
        self.roomAccusation.setItemText(1, _translate("AccusationDialog", "Conservatory"))
        self.roomAccusation.setItemText(2, _translate("AccusationDialog", "Study"))
        self.roomAccusation.setItemText(3, _translate("AccusationDialog", "Billiard Room"))
        self.roomAccusation.setItemText(4, _translate("AccusationDialog", "Dining Room"))
        self.roomAccusation.setItemText(5, _translate("AccusationDialog", "Kitchen"))
        self.roomAccusation.setItemText(6, _translate("AccusationDialog", "Library"))
        self.roomAccusation.setItemText(7, _translate("AccusationDialog", "Hall"))
        self.roomAccusation.setItemText(8, _translate("AccusationDialog", "Lounge"))
        self.roomAccusation.setItemText(9, _translate("AccusationDialog", "Ballroom"))

