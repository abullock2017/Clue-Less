# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\EmptySuggestionResponse.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_emptySuggestionResponse(object):
    def setupUi(self, emptySuggestionResponse):
        emptySuggestionResponse.setObjectName("emptySuggestionResponse")
        emptySuggestionResponse.resize(400, 300)
        self.emptyResponseButtonBox = QtWidgets.QDialogButtonBox(emptySuggestionResponse)
        self.emptyResponseButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.emptyResponseButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.emptyResponseButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.emptyResponseButtonBox.setCenterButtons(True)
        self.emptyResponseButtonBox.setObjectName("emptyResponseButtonBox")
        self.responseExplanation = QtWidgets.QLabel(emptySuggestionResponse)
        self.responseExplanation.setGeometry(QtCore.QRect(50, 110, 301, 31))
        self.responseExplanation.setAlignment(QtCore.Qt.AlignCenter)
        self.responseExplanation.setObjectName("responseExplanation")

        self.retranslateUi(emptySuggestionResponse)
        self.emptyResponseButtonBox.accepted.connect(emptySuggestionResponse.accept)
        self.emptyResponseButtonBox.rejected.connect(emptySuggestionResponse.reject)
        QtCore.QMetaObject.connectSlotsByName(emptySuggestionResponse)

    def retranslateUi(self, emptySuggestionResponse):
        _translate = QtCore.QCoreApplication.translate
        emptySuggestionResponse.setWindowTitle(_translate("emptySuggestionResponse", "Suggestion Response"))
        self.responseExplanation.setText(_translate("emptySuggestionResponse", "No players have your suggestions."))

