# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\m01_YourTurnDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YourTurnDialog(object):
    def setupUi(self, YourTurnDialog):
        YourTurnDialog.setObjectName("YourTurnDialog")
        YourTurnDialog.resize(400, 300)
        self.turnButtonBox = QtWidgets.QDialogButtonBox(YourTurnDialog)
        self.turnButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.turnButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.turnButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.turnButtonBox.setCenterButtons(True)
        self.turnButtonBox.setObjectName("turnButtonBox")
        self.yourTurnLabel = QtWidgets.QLabel(YourTurnDialog)
        self.yourTurnLabel.setGeometry(QtCore.QRect(50, 110, 301, 31))
        self.yourTurnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yourTurnLabel.setObjectName("yourTurnLabel")

        self.retranslateUi(YourTurnDialog)
        self.turnButtonBox.accepted.connect(YourTurnDialog.accept)
        self.turnButtonBox.rejected.connect(YourTurnDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(YourTurnDialog)

    def retranslateUi(self, YourTurnDialog):
        _translate = QtCore.QCoreApplication.translate
        YourTurnDialog.setWindowTitle(_translate("YourTurnDialog", "Your Turn"))
        self.yourTurnLabel.setText(_translate("YourTurnDialog", "Your turn!"))

