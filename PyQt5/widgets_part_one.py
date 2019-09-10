"""
PyQt的部分组件，比如勾选框，按钮，滑动条，进度条，日历组件
"""
import sys


def checkbox():
    """

    """
    from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
    from PyQt5.QtCore import Qt

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):

            cb = QCheckBox('Show title', self)
            cb.move(20, 20)
            cb.toggle()  # 使用setChecked 也会被触发
            cb.stateChanged.connect(self.changeTitle)

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('QCheckBox')
            self.show()

        def changeTitle(self, state):

            if state == Qt.Checked:
                self.setWindowTitle('QCheckBox')
            else:
                self.setWindowTitle(' ')

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def toggle_button():
    """
    可以长按的按钮
    """
    from PyQt5.QtWidgets import (QWidget, QPushButton,
                                 QFrame, QApplication)
    from PyQt5.QtGui import QColor

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.col = QColor(0, 0, 0)
            redb = QPushButton('Red', self)
            redb.setCheckable(True)  # 使按钮可以保持在 pressed 的状态
            redb.move(10, 10)

            redb.clicked[bool].connect(self.setColor)
            greenb = QPushButton('Green', self)
            greenb.setCheckable(True)
            greenb.move(10, 60)

            greenb.clicked[bool].connect(self.setColor)

            blueb = QPushButton('Blue', self)
            blueb.setCheckable(True)
            blueb.move(10, 110)

            blueb.clicked[bool].connect(self.setColor)

            # 初始化颜色框
            self.square = QFrame(self)
            self.square.setGeometry(150, 20, 100, 100)
            self.square.setStyleSheet("QWidget { background-color: %s }" %
                                      self.col.name())

            self.setGeometry(300, 300, 280, 170)
            self.setWindowTitle('Toggle button')
            self.show()

        def setColor(self, pressed):
            """
            修改颜色
            """
            source = self.sender()  # 获取触发源
            if pressed:
                val = 255
            else:
                val = 0
            if source.text() == "Red":
                self.col.setRed(val)
            elif source.text() == "Green":
                self.col.setGreen(val)
            else:
                self.col.setBlue(val)
            self.square.setStyleSheet("QFrame { background-color: %s }" %
                                      self.col.name())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def slider():
    """
    滑动条的组件
    """
    from PyQt5.QtWidgets import (QWidget, QSlider,
                                 QLabel, QApplication)
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QPixmap

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):

            sld = QSlider(Qt.Horizontal, self)
            sld.setFocusPolicy(Qt.NoFocus)  # 配置获取焦点的策略，没有焦点
            sld.setGeometry(30, 40, 100, 30)
            sld.valueChanged[int].connect(self.changeValue)

            self.label = QLabel(self)
            self.label.setPixmap(QPixmap('resources/speaker__easy_0.png'))
            self.label.setGeometry(160, 40, 80, 32)

            self.setGeometry(300, 300, 280, 170)
            self.setWindowTitle('QSlider')
            self.show()

        def changeValue(self, value):
            """
            根据滑动的值修改图片展示
            """
            if value == 0:
                self.label.setPixmap(QPixmap('resources/speaker__easy_0.png'))
            elif value > 0 and value <= 30:
                self.label.setPixmap(QPixmap('resources/speaker__easy_1.png'))
            elif value > 30 and value < 80:
                self.label.setPixmap(QPixmap('resources/speaker__easy_2.png'))
            else:
                self.label.setPixmap(QPixmap('resources/speaker__easy_3.png'))

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def progress_bar():
    """
    进度条
    """
    from PyQt5.QtWidgets import (QWidget, QProgressBar,
                                 QPushButton, QApplication)
    from PyQt5.QtCore import QBasicTimer

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 创建进度条
            self.pbar = QProgressBar(self)
            self.pbar.setGeometry(30, 40, 200, 25)
            # 创建开始按钮
            self.btn = QPushButton('Start', self)
            self.btn.move(40, 80)
            self.btn.clicked.connect(self.doAction)
            # 创建计时器，初始化计数
            self.timer = QBasicTimer()
            self.step = 0

            self.setGeometry(300, 300, 280, 170)
            self.setWindowTitle('QProgressBar')
            self.show()

        def timerEvent(self, e):
            if self.step >= 100:
                self.timer.stop()
                self.btn.setText('Finished')
                return

            self.step = self.step + 1
            self.pbar.setValue(self.step)

        def doAction(self):

            if self.timer.isActive():
                self.timer.stop()
                self.btn.setText('Start')
            else:
                self.timer.start(100, self)
                self.btn.setText('Stop')

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def calendar():
    """
    日历组件
    """
    from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                                 QLabel, QApplication, QVBoxLayout)
    from PyQt5.QtCore import QDate

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):

            vbox = QVBoxLayout(self)  # 创建布局
            cal = QCalendarWidget(self)  # 创建日历组件
            cal.setGridVisible(True)  # 设置日历网格可见
            cal.clicked[QDate].connect(self.showDate)
            vbox.addWidget(cal)

            self.lbl = QLabel(self)
            date = cal.selectedDate()
            self.lbl.setText(date.toString())

            vbox.addWidget(self.lbl)

            self.setLayout(vbox)

            self.setGeometry(300, 300, 350, 300)
            self.setWindowTitle('Calendar')
            self.show()

        def showDate(self, date):
            self.lbl.setText(date.toString())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# checkbox()
# toggle_button()
# slider()
# progress_bar()
calendar()
