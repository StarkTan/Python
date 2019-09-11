# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'childjiemian.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_W2(object):
    def setupUi(self, W2):
        W2.setObjectName("W2")
        W2.resize(473, 409)
        self.label = QtWidgets.QLabel(W2)
        self.label.setGeometry(QtCore.QRect(50, 120, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(W2)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 121, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(W2)
        self.lineEdit.setGeometry(QtCore.QRect(210, 120, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(W2)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 180, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(W2)
        self.pushButton.setGeometry(QtCore.QRect(160, 290, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(W2)
        self.label_3.setGeometry(QtCore.QRect(160, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(W2)
        QtCore.QMetaObject.connectSlotsByName(W2)

    def retranslateUi(self, W2):
        _translate = QtCore.QCoreApplication.translate
        W2.setWindowTitle(_translate("W2", "Form"))
        self.label.setText(_translate("W2", "给父窗体发送数据："))
        self.label_2.setText(_translate("W2", "接收父窗体数据："))
        self.pushButton.setText(_translate("W2", "向父窗体发送数据"))
        self.label_3.setText(_translate("W2", "子窗体"))

