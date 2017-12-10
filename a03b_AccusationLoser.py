# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\a03b_AccusationLoser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YouLoseDialog(object):
    def setupUi(self, YouLoseDialog):
        YouLoseDialog.setObjectName("YouLoseDialog")
        YouLoseDialog.resize(400, 300)
        self.YouLoseButtons = QtWidgets.QDialogButtonBox(YouLoseDialog)
        self.YouLoseButtons.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.YouLoseButtons.setOrientation(QtCore.Qt.Horizontal)
        self.YouLoseButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.YouLoseButtons.setCenterButtons(True)
        self.YouLoseButtons.setObjectName("YouLoseButtons")
        self.loserNameLabel = QtWidgets.QLabel(YouLoseDialog)
        self.loserNameLabel.setGeometry(QtCore.QRect(130, 100, 131, 31))
        self.loserNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loserNameLabel.setObjectName("loserNameLabel")
        self.lossActionLabel = QtWidgets.QLabel(YouLoseDialog)
        self.lossActionLabel.setGeometry(QtCore.QRect(50, 130, 301, 31))
        self.lossActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lossActionLabel.setObjectName("lossActionLabel")

        self.retranslateUi(YouLoseDialog)
        self.YouLoseButtons.accepted.connect(YouLoseDialog.accept)
        self.YouLoseButtons.rejected.connect(YouLoseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(YouLoseDialog)

    def retranslateUi(self, YouLoseDialog):
        _translate = QtCore.QCoreApplication.translate
        YouLoseDialog.setWindowTitle(_translate("YouLoseDialog", "You Lose!"))
        self.loserNameLabel.setText(_translate("YouLoseDialog", "TextLabel"))
        self.lossActionLabel.setText(_translate("YouLoseDialog", "has lost the game."))

