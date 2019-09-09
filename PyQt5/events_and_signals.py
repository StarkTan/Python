"""
事件和信号的响应
"""
import sys


def signals_and_slots():
    """"""

    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                                 QVBoxLayout, QApplication)

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 创建数字展示组件和滑动条
            lcd = QLCDNumber(self)
            sld = QSlider(Qt.Horizontal, self)
            # 构建垂直布局
            vbox = QVBoxLayout()
            vbox.addWidget(lcd)
            vbox.addWidget(sld)
            self.setLayout(vbox)
            # 绑定滑动条的数据到数字组件上
            sld.valueChanged.connect(lcd.display)

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Signal and slot')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def reimplementing_event_handler():
    """
    重新实现 Event 处理
    """
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QWidget, QApplication

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Event handler')
            self.show()

        def keyPressEvent(self, e):
            """
            重写按键响应
            """
            if e.key() == Qt.Key_Escape:
                self.close()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def event_object():
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 初始化展示的信息
            x = 0
            y = 0
            self.text = "x: {0},  y: {1}".format(x, y)
            self.label = QLabel(self.text, self)

            # 配置布局和内容
            grid = QGridLayout()
            grid.addWidget(self.label, 0, 0, Qt.AlignTop)
            self.setLayout(grid)

            # 开启鼠标捕捉
            self.setMouseTracking(True)

            self.setGeometry(300, 300, 350, 200)
            self.setWindowTitle('Event object')
            self.show()

        def mouseMoveEvent(self, e):
            """
            重写鼠标移动事件
            """
            x = e.x()
            y = e.y()

            text = "x: {0},  y: {1}".format(x, y)
            self.label.setText(text)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def event_sender():
    """
    使用 sender 获取事件源
    """
    from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

    class Example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 创建按钮和绑定点击事件
            btn1 = QPushButton("Button 1", self)
            btn1.move(30, 50)
            btn2 = QPushButton("Button 2", self)
            btn2.move(150, 50)
            btn1.clicked.connect(self.buttonClicked)
            btn2.clicked.connect(self.buttonClicked)
            self.statusBar()
            self.setGeometry(300, 300, 290, 150)
            self.setWindowTitle('Event sender')
            self.show()

        def buttonClicked(self):
            # 使用sender() 获取事件触发源
            sender = self.sender()
            self.statusBar().showMessage(sender.text() + ' was pressed')

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def custom_signal():
    from PyQt5.QtCore import pyqtSignal, QObject
    from PyQt5.QtWidgets import QMainWindow, QApplication

    class Communicate(QObject):
        """
        集成 QObeject 的类可以发送信号
        """
        closeApp = pyqtSignal()

    class Example(QMainWindow):
        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            # 创建自定义对象
            self.c = Communicate()
            # 为自定义对象连接对象
            self.c.closeApp.connect(self.close)

            self.setGeometry(300, 300, 290, 150)
            self.setWindowTitle('Emit signal')
            self.show()

        def mousePressEvent(self, event):
            """
            修改鼠标 press 事件，使自定义对象发送信号
            """
            self.c.closeApp.emit()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# signals_and_slots()
# reimplementing_event_handler()
# event_object()
# event_sender()
custom_signal()
