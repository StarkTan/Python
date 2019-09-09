"""
会话框 PyQt的对话框只数据输入框
"""

import sys


def input_dialog():
    """
    简单的 Input 输入框
    """
    from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                                 QInputDialog, QApplication)

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.btn = QPushButton('Dialog', self)
            self.btn.move(20, 20)
            self.btn.clicked.connect(self.showDialog)

            self.le = QLineEdit(self)
            self.le.move(130, 22)

            self.setGeometry(300, 300, 290, 150)
            self.setWindowTitle('Input dialog')
            self.show()

        def showDialog(self):
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                                            'Enter your name:')

            if ok:
                self.le.setText(str(text))

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def color_dialog():
    """
    颜色选择交互
    """
    from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                                 QColorDialog, QApplication)
    from PyQt5.QtGui import QColor

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            col = QColor(0, 0, 0)
            self.btn = QPushButton('Dialog', self)
            self.btn.move(20, 20)
            self.btn.clicked.connect(self.showDialog)

            # 添加QFrame组件，配置背景颜色背景颜色
            self.frm = QFrame(self)
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

            self.frm.setGeometry(130, 22, 100, 100)
            self.setGeometry(300, 300, 250, 180)
            self.setWindowTitle('Color dialog')
            self.show()

        def showDialog(self):
            # 弹出颜色选择框，选取颜色值
            col = QColorDialog.getColor()
            if col.isValid():
                self.frm.setStyleSheet("QWidget { background-color: %s }"
                                       % col.name())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def font_dialog():
    """
    字体选择对话框
    """
    from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                                 QSizePolicy, QLabel, QFontDialog, QApplication)

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 创建初始化元素
            vbox = QVBoxLayout()
            btn = QPushButton('Dialog', self)
            btn.setSizePolicy(QSizePolicy.Fixed,
                              QSizePolicy.Fixed)
            btn.move(20, 20)
            vbox.addWidget(btn)
            btn.clicked.connect(self.showDialog)
            self.lbl = QLabel('Knowledge only matters', self)
            self.lbl.move(130, 20)
            vbox.addWidget(self.lbl)
            self.setLayout(vbox)

            self.setGeometry(300, 300, 250, 180)
            self.setWindowTitle('Font dialog')
            self.show()

        def showDialog(self):
            # 弹出字体选择框，选择字体
            font, ok = QFontDialog.getFont()
            if ok:
                self.lbl.setFont(font)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def file_dialog():
    """
    文件选择交互框
    """
    from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                                 QAction, QFileDialog, QApplication)
    from PyQt5.QtGui import QIcon

    class Example(QMainWindow):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            # 创建主体为一个编辑框
            self.textEdit = QTextEdit()
            self.setCentralWidget(self.textEdit)
            self.statusBar()

            # 创建Open文件的选项
            openFile = QAction(QIcon('open.png'), 'Open', self)
            openFile.setShortcut('Ctrl+O')
            openFile.setStatusTip('Open new File')
            openFile.triggered.connect(self.showDialog)

            # 配置菜单栏
            menubar = self.menuBar()
            fileMenu = menubar.addMenu('&File')
            fileMenu.addAction(openFile)

            self.setGeometry(300, 300, 350, 300)
            self.setWindowTitle('File dialog')
            self.show()

        def showDialog(self):
            # 打开文件选择框
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
            # 读取文件数据展示
            if fname[0]:
                f = open(fname[0], 'r')
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
                f.close()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# input_dialog()
# color_dialog()
# font_dialog()
file_dialog()
