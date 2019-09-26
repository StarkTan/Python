import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import  QObject

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        quit_btn = QPushButton('Quit', self)
        quit_btn.clicked.connect(self.print_msg)  # QApplication.instance().quit

        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


    def print_msg(self):
        print(QApplication.instance())
        print(QApplication.instance().datacenter)

class DataCenter(QObject):
    def __init__(self):
        super().__init__()
        self.name = 'test'


app = QApplication(sys.argv)
app.datacenter=DataCenter()
print(app)
ex = Example()
sys.exit(app.exec_())