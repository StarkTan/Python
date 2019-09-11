# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:53:30 2018

@author: Administrator
"""

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
from mainfilejiemian import Ui_W1
from child import W2

class W1(QWidget, Ui_W1):
    parentclicked = pyqtSignal(str)   

    def __init__(self, parent=None):
        super(W1, self).__init__(parent)        
        self.setupUi(self)
        self.w2 = W2()
        self.pushButton.clicked.connect(self.child)
        self.pushButton_2.clicked.connect(self.parentsend)
        self.parentclicked.connect(self.recv2)  #  父窗体向子窗体传数据的“信号与槽连接”
        
    def child(self):
        # self.w2 = W2()
        self.w2.childclicked.connect(self.recv)  #  字窗体向父窗体传数据的“信号与槽连接”
        self.w2.show()

    # 父窗体向子窗体传数据
    def parentsend(self):
        parentstr = self.lineEdit_2.text()  # 父窗体输入的字符，发送给子窗体
        self.parentclicked.emit(parentstr)  #  父窗体向子窗体发射信号

    # 槽函数，父窗体接收子窗体的数据
    def recv(self, s):
        self.lineEdit.setText(s)

    # 槽函数，子窗体接收父窗体的数据
    def recv2(self, s):
        self.w2.lineEdit_2.setText(s)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = W1()
    ui.show()
    sys.exit(app.exec_())
