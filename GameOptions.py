# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\GameOptions.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GameOptions(object):
    def setupUi(self, GameOptions):
        GameOptions.setObjectName("GameOptions")
        GameOptions.resize(400, 300)
        self.gameOptionsButtonBox = QtWidgets.QDialogButtonBox(GameOptions)
        self.gameOptionsButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.gameOptionsButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.gameOptionsButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.gameOptionsButtonBox.setCenterButtons(True)
        self.gameOptionsButtonBox.setObjectName("gameOptionsButtonBox")
        self.gameMusicSlider_2 = QtWidgets.QGroupBox(GameOptions)
        self.gameMusicSlider_2.setGeometry(QtCore.QRect(50, 50, 301, 71))
        self.gameMusicSlider_2.setObjectName("gameMusicSlider_2")
        self.gameMusicSlider = QtWidgets.QSlider(self.gameMusicSlider_2)
        self.gameMusicSlider.setGeometry(QtCore.QRect(20, 30, 261, 22))
        self.gameMusicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gameMusicSlider.setObjectName("gameMusicSlider")
        self.gameEffectsBox = QtWidgets.QGroupBox(GameOptions)
        self.gameEffectsBox.setGeometry(QtCore.QRect(50, 140, 301, 71))
        self.gameEffectsBox.setObjectName("gameEffectsBox")
        self.gameEffectsSlider = QtWidgets.QSlider(self.gameEffectsBox)
        self.gameEffectsSlider.setGeometry(QtCore.QRect(20, 30, 261, 22))
        self.gameEffectsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gameEffectsSlider.setObjectName("gameEffectsSlider")

        self.retranslateUi(GameOptions)
        self.gameOptionsButtonBox.accepted.connect(GameOptions.accept)
        self.gameOptionsButtonBox.rejected.connect(GameOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(GameOptions)

    def retranslateUi(self, GameOptions):
        _translate = QtCore.QCoreApplication.translate
        GameOptions.setWindowTitle(_translate("GameOptions", "Sound Options"))
        self.gameMusicSlider_2.setTitle(_translate("GameOptions", "Music"))
        self.gameEffectsBox.setTitle(_translate("GameOptions", "Sound Effects"))

