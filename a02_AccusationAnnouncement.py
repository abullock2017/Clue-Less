# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eclipse-oxygen-workspace\Clue-Less\a02_AccusationAnnouncement.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccusationAnnouncementDialog(object):
    def setupUi(self, AccusationAnnouncementDialog):
        AccusationAnnouncementDialog.setObjectName("AccusationAnnouncementDialog")
        AccusationAnnouncementDialog.resize(400, 300)
        self.AccusationAnnouncementButtons = QtWidgets.QDialogButtonBox(AccusationAnnouncementDialog)
        self.AccusationAnnouncementButtons.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.AccusationAnnouncementButtons.setOrientation(QtCore.Qt.Horizontal)
        self.AccusationAnnouncementButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.AccusationAnnouncementButtons.setCenterButtons(True)
        self.AccusationAnnouncementButtons.setObjectName("AccusationAnnouncementButtons")
        self.accuserName = QtWidgets.QLabel(AccusationAnnouncementDialog)
        self.accuserName.setGeometry(QtCore.QRect(130, 30, 131, 31))
        self.accuserName.setAlignment(QtCore.Qt.AlignCenter)
        self.accuserName.setObjectName("accuserName")
        self.accusedWeapon = QtWidgets.QLabel(AccusationAnnouncementDialog)
        self.accusedWeapon.setGeometry(QtCore.QRect(170, 120, 61, 91))
        self.accusedWeapon.setAutoFillBackground(True)
        self.accusedWeapon.setText("")
        self.accusedWeapon.setPixmap(QtGui.QPixmap("leadPipeCard.jpg"))
        self.accusedWeapon.setScaledContents(True)
        self.accusedWeapon.setAlignment(QtCore.Qt.AlignCenter)
        self.accusedWeapon.setObjectName("accusedWeapon")
        self.accusedRoom = QtWidgets.QLabel(AccusationAnnouncementDialog)
        self.accusedRoom.setGeometry(QtCore.QRect(270, 120, 61, 91))
        self.accusedRoom.setAutoFillBackground(True)
        self.accusedRoom.setText("")
        self.accusedRoom.setPixmap(QtGui.QPixmap("loungeCard.jpg"))
        self.accusedRoom.setScaledContents(True)
        self.accusedRoom.setAlignment(QtCore.Qt.AlignCenter)
        self.accusedRoom.setObjectName("accusedRoom")
        self.accusedCharacter = QtWidgets.QLabel(AccusationAnnouncementDialog)
        self.accusedCharacter.setGeometry(QtCore.QRect(70, 120, 61, 91))
        self.accusedCharacter.setAutoFillBackground(True)
        self.accusedCharacter.setText("")
        self.accusedCharacter.setPixmap(QtGui.QPixmap("peacock.jpg"))
        self.accusedCharacter.setScaledContents(True)
        self.accusedCharacter.setAlignment(QtCore.Qt.AlignCenter)
        self.accusedCharacter.setObjectName("accusedCharacter")
        self.accusationLabel = QtWidgets.QLabel(AccusationAnnouncementDialog)
        self.accusationLabel.setGeometry(QtCore.QRect(50, 60, 301, 31))
        self.accusationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.accusationLabel.setObjectName("accusationLabel")

        self.retranslateUi(AccusationAnnouncementDialog)
        self.AccusationAnnouncementButtons.accepted.connect(AccusationAnnouncementDialog.accept)
        self.AccusationAnnouncementButtons.rejected.connect(AccusationAnnouncementDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccusationAnnouncementDialog)

    def retranslateUi(self, AccusationAnnouncementDialog):
        _translate = QtCore.QCoreApplication.translate
        AccusationAnnouncementDialog.setWindowTitle(_translate("AccusationAnnouncementDialog", "Accusation Made"))
        self.accuserName.setText(_translate("AccusationAnnouncementDialog", "TextLabel"))
        self.accusationLabel.setText(_translate("AccusationAnnouncementDialog", "has made the following accusation:"))

