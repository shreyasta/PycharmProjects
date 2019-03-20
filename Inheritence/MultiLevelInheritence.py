# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiLevelInheritence.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(897, 989)
        self.StudentCode = QtWidgets.QLabel(Dialog)
        self.StudentCode.setGeometry(QtCore.QRect(50, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StudentCode.setFont(font)
        self.StudentCode.setObjectName("StudentCode")
        self.StudentName = QtWidgets.QLabel(Dialog)
        self.StudentName.setGeometry(QtCore.QRect(50, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StudentName.setFont(font)
        self.StudentName.setObjectName("StudentName")
        self.HistoryMarks = QtWidgets.QLabel(Dialog)
        self.HistoryMarks.setGeometry(QtCore.QRect(50, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HistoryMarks.setFont(font)
        self.HistoryMarks.setObjectName("HistoryMarks")
        self.GeographyMarks = QtWidgets.QLabel(Dialog)
        self.GeographyMarks.setGeometry(QtCore.QRect(50, 220, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GeographyMarks.setFont(font)
        self.GeographyMarks.setObjectName("GeographyMarks")
        self.Total = QtWidgets.QLabel(Dialog)
        self.Total.setGeometry(QtCore.QRect(50, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Total.setFont(font)
        self.Total.setObjectName("Total")
        self.Percentage = QtWidgets.QLabel(Dialog)
        self.Percentage.setGeometry(QtCore.QRect(50, 330, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Percentage.setFont(font)
        self.Percentage.setObjectName("Percentage")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(210, 80, 221, 31))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(210, 130, 221, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditHistorymarks = QtWidgets.QLineEdit(Dialog)
        self.lineEditHistorymarks.setGeometry(QtCore.QRect(210, 180, 221, 31))
        self.lineEditHistorymarks.setObjectName("lineEditHistorymarks")
        self.lineEditGeographyMarks = QtWidgets.QLineEdit(Dialog)
        self.lineEditGeographyMarks.setGeometry(QtCore.QRect(210, 230, 221, 31))
        self.lineEditGeographyMarks.setObjectName("lineEditGeographyMarks")
        self.lineEditTotal = QtWidgets.QLineEdit(Dialog)
        self.lineEditTotal.setEnabled(False)
        self.lineEditTotal.setGeometry(QtCore.QRect(210, 290, 221, 31))
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.lineEditPercentage = QtWidgets.QLineEdit(Dialog)
        self.lineEditPercentage.setEnabled(False)
        self.lineEditPercentage.setGeometry(QtCore.QRect(210, 340, 221, 31))
        self.lineEditPercentage.setObjectName("lineEditPercentage")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(220, 420, 141, 41))
        self.ButtonClickMe.setObjectName("Click")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.StudentCode.setText(_translate("Dialog", "Student code"))
        self.StudentName.setText(_translate("Dialog", "Student name"))
        self.HistoryMarks.setText(_translate("Dialog", "History marks"))
        self.GeographyMarks.setText(_translate("Dialog", "Geography marks"))
        self.Total.setText(_translate("Dialog", "Total"))
        self.Percentage.setText(_translate("Dialog", "Percentage"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))

