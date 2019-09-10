"""
PyQt的部分组件，比如勾选框，按钮，滑动条，进度条，日历组件
"""
import sys


def pixmap():
    """
    图片加载
    """
    from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                                 QLabel, QApplication)
    from PyQt5.QtGui import QPixmap

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            hbox = QHBoxLayout(self)
            pixmap = QPixmap("pyqt.jpg")  # 加载图片

            lbl = QLabel(self)
            lbl.setPixmap(pixmap)

            hbox.addWidget(lbl)  # 将图片放入需要的组件
            self.setLayout(hbox)

            self.move(300, 200)
            self.setWindowTitle('PyQt')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def line_edit():
    """
    输入框
    """
    from PyQt5.QtWidgets import (QWidget, QLabel,
                                 QLineEdit, QApplication)

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.lbl = QLabel(self)
            qle = QLineEdit(self)

            qle.move(60, 100)
            self.lbl.move(60, 40)

            # 绑定输入变化事件的处理
            qle.textChanged[str].connect(self.onChanged)

            self.setGeometry(300, 300, 280, 170)
            self.setWindowTitle('QLineEdit')
            self.show()

        def onChanged(self, text):
            self.lbl.setText(text)
            self.lbl.adjustSize()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def splitter():
    """
    窗口切割
    TODO 实现 QSplitter 的大小控制
    """
    from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                                 QSplitter, QStyleFactory, QApplication)
    from PyQt5.QtCore import Qt

    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            hbox = QHBoxLayout(self)

            topleft = QFrame(self)
            topleft.setFrameShape(QFrame.StyledPanel)  # 设置边框类型

            topright = QFrame(self)
            topright.setFrameShape(QFrame.StyledPanel)

            bottom = QFrame(self)
            bottom.setFrameShape(QFrame.StyledPanel)

            splitter1 = QSplitter(Qt.Horizontal)
            splitter1.addWidget(topleft)
            splitter1.addWidget(topright)

            splitter2 = QSplitter(Qt.Vertical)
            splitter2.addWidget(splitter1)
            splitter2.addWidget(bottom)

            hbox.addWidget(splitter2)
            self.setLayout(hbox)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('QSplitter')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def combobox():
    """
    下拉选择框
    """
    from PyQt5.QtWidgets import (QWidget, QLabel,
                                 QComboBox, QApplication)

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.lbl = QLabel("Ubuntu", self)

            combo = QComboBox(self)
            combo.addItem("Ubuntu")
            combo.addItem("Mandriva")
            combo.addItem("Fedora")
            combo.addItem("Arch")
            combo.addItem("Gentoo")

            combo.move(50, 50)
            self.lbl.move(50, 150)

            # 绑定选择事件
            combo.activated[str].connect(self.onActivated)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('QComboBox')
            self.show()

        def onActivated(self, text):
            self.lbl.setText(text)
            self.lbl.adjustSize()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# pixmap()
# line_edit()
# splitter()
combobox()
