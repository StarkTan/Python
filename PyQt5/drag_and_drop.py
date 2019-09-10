"""
PyQt的文件拖拽接收
"""

import sys


def simple_drag_drop():
    """
    简单的拖拽
    """
    from PyQt5.QtWidgets import (QPushButton, QWidget,
                                 QLineEdit, QApplication)

    class Button(QPushButton):
        """
        自定义按钮 继承QPushButton
        """
        def __init__(self, title, parent):
            super().__init__(title, parent)
            # 设置可拖拽
            self.setAcceptDrops(True)

        def dragEnterEvent(self, e):

            if e.mimeData().hasFormat('text/uri-list'):
                e.accept()
            else:
                e.ignore()

        def dropEvent(self, e):

            self.setText(e.mimeData().text())

    class LineEdit(QLineEdit):
        """
        自定义输入框 继承QPushButton
        """
        def __init__(self, *__args):
            super().__init__(*__args)
            # 设置可拖拽
            self.setAcceptDrops(True)

        def dragEnterEvent(self, e):
            if e.mimeData().hasFormat('text/uri-list'):
                e.accept()
            else:
                e.ignore()

        def dropEvent(self, e):

            self.setText(e.mimeData().text())

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            edit = LineEdit('', self)
            edit.setDragEnabled(True)
            edit.move(30, 65)

            button = Button("Button", self)
            button.move(190, 65)

            self.setWindowTitle('Simple drag and drop')
            self.setGeometry(300, 300, 300, 150)

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


def drag_button():
    """
    实现左键点击，右键拖拽按钮
    """
    from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
    from PyQt5.QtCore import Qt, QMimeData
    from PyQt5.QtGui import QDrag

    class Button(QPushButton):
        def __init__(self, title, parent):
            super().__init__(title, parent)

        def mouseMoveEvent(self, e):

            if e.buttons() != Qt.RightButton:
                return

            mimeData = QMimeData()

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(e.pos() - self.rect().topLeft())  # 设置位置

            # 执行移动
            dropAction = drag.exec_(Qt.MoveAction)

        def mousePressEvent(self, e):
            super().mousePressEvent(e)

            if e.button() == Qt.LeftButton:
                print('press')

    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setAcceptDrops(True)

            self.button = Button('Button', self)
            self.button.move(100, 65)

            self.setWindowTitle('Click or Move')
            self.setGeometry(300, 300, 280, 150)

        def dragEnterEvent(self, e):
            e.accept()

        def dropEvent(self, e):
            position = e.pos()
            self.button.move(position)

            e.setDropAction(Qt.MoveAction)
            e.accept()

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


# simple_drag_drop()
drag_button()
