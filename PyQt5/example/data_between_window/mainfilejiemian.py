# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainfilejiemian.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_W1(object):
    def setupUi(self, W1):
        W1.setObjectName("W1")
        W1.resize(463, 475)
        self.label = QtWidgets.QLabel(W1)
        self.label.setGeometry(QtCore.QRect(40, 130, 131, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(W1)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 131, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(W1)
        self.lineEdit.setGeometry(QtCore.QRect(180, 140, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(W1)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 220, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(W1)
        self.pushButton.setGeometry(QtCore.QRect(50, 340, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(W1)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 340, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(W1)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(W1)
        QtCore.QMetaObject.connectSlotsByName(W1)

    def retranslateUi(self, W1):
        _translate = QtCore.QCoreApplication.translate
        W1.setWindowTitle(_translate("W1", "Form"))
        self.label.setText(_translate("W1", "接收子窗体数据："))
        self.label_2.setText(_translate("W1", "给子窗体发送数据："))
        self.pushButton.setText(_translate("W1", "打开子窗体"))
        self.pushButton_2.setText(_translate("W1", "向子窗体发送数据"))
        self.label_3.setText(_translate("W1", "主窗体"))

