"""
PyQt 的布局设置
"""
import sys


def absolute():
    """
    指定相对窗口左上角的位置
    """
    from PyQt5.QtWidgets import QWidget, QLabel, QApplication

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            lbl1 = QLabel('Zetcode', self)
            # 指定固定的位置
            lbl1.move(15, 10)

            lbl2 = QLabel('tutorials', self)
            lbl2.move(35, 40)

            lbl3 = QLabel('for programmers', self)
            lbl3.move(55, 70)

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Absolute')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def box_layout():
    """
    垂直、水平布局
    例子是将两个按钮水平放置在右下角
    """
    from PyQt5.QtWidgets import (QWidget, QPushButton,
                                 QHBoxLayout, QVBoxLayout, QApplication)

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 创建两个按钮
            okButton = QPushButton("OK")
            cancelButton = QPushButton("Cancel")

            # 创建一个水平布局，放入两个按钮
            hbox = QHBoxLayout()
            hbox.addStretch(1)  # 添加一个伸缩量，可以看做左边填满
            hbox.addWidget(okButton)
            hbox.addWidget(cancelButton)

            # 创建一个垂直布局，加入上一个水平布局
            vbox = QVBoxLayout()
            vbox.addStretch(1)
            vbox.addLayout(hbox)

            # 设置主窗口布局是垂直布局
            self.setLayout(vbox)

            self.setGeometry(300, 300, 300, 150)
            self.setWindowTitle('Buttons')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def grid_calculator():
    """
    使用 Grid 布局做的计算器
    """
    from PyQt5.QtWidgets import (QWidget, QGridLayout,
                                 QPushButton, QApplication)

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 设置窗口布局为Grid
            grid = QGridLayout()
            self.setLayout(grid)

            names = ['Cls', 'Bck', '', 'Close',
                     '7', '8', '9', '/',
                     '4', '5', '6', '*',
                     '1', '2', '3', '-',
                     '0', '.', '=', '+']

            positions = [(i, j) for i in range(5) for j in range(4)]

            for position, name in zip(positions, names):
                if name == '':
                    continue
                button = QPushButton(name)
                grid.addWidget(button, *position)

            self.move(300, 150)
            self.setWindowTitle('Calculator')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def grid_review():
    from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                                 QTextEdit, QGridLayout, QApplication)

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            # 创建输入框标签
            title = QLabel('Title')
            author = QLabel('Author')
            review = QLabel('Review')
            # 创建输入框
            titleEdit = QLineEdit()
            authorEdit = QLineEdit()
            reviewEdit = QTextEdit()
            # 创建 grid 布局
            grid = QGridLayout()
            # 设置间隙
            grid.setSpacing(10)

            grid.addWidget(title, 1, 0)
            grid.addWidget(titleEdit, 1, 1)

            grid.addWidget(author, 2, 0)
            grid.addWidget(authorEdit, 2, 1)

            grid.addWidget(review, 3, 0)
            grid.addWidget(reviewEdit, 3, 1, 5, 1)

            self.setLayout(grid)

            self.setGeometry(300, 300, 350, 300)
            self.setWindowTitle('Review')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# absolute()
# box_layout()
# grid_calculator()
grid_review()
