# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:58:29 2018

@author: Administrator
"""

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from childjiemian import Ui_W2

class W2(QWidget,Ui_W2):
    childclicked = pyqtSignal(str)  

    def __init__(self, parent=None):
        super(W2, self).__init__(parent)        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.childsend)
    
    def childsend(self):
        childstr = self.lineEdit.text()  #  子窗体输入的字符，发送给父窗体
        self.childclicked.emit(childstr)  #  子窗体向父窗体发射信号