"""
展示PyQt5的的一些基本功能，
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


def simple():
    """
    最简单的一个窗体
    """
    app = QApplication(sys.argv)  # PyQt5 必须创建一个 Application 对象
    w = QWidget(flags=Qt.WindowFlags())  # QWidget 是最基础的交互类
    w.resize(250, 150)  # 设置窗口的大小
    w.move(300, 300)  # 设置窗口左上角位置
    w.setWindowTitle('Simple')  #设置窗口的Window
    w.show()  # 展示窗口
    app.exec_()  # 启动应用
    sys.exit()   # 进程退出


def icon():
    """
    简单的图标
    """
    from PyQt5.QtGui import QIcon

    class Example(QWidget):
        def __init__(self):
            """
            继承 Qwidget，执行 initUI（）来构建内容
            """
            super().__init__(flags=Qt.WindowFlags())
            self.initUI()

        def initUI(self):
            """
            配置窗口初始化时候需要展示的内容
            """
            self.setGeometry(300, 300, 300, 220)  # 参数  x，y，width， height
            self.setWindowTitle('Icon')
            self.setWindowIcon(QIcon('pyqt.jpg'))  # 加载 Icon 图片
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def tooltip():
    """
    创建按钮和提示消息
    """
    from PyQt5.QtWidgets import (QWidget, QToolTip,
                                 QPushButton, QApplication)
    from PyQt5.QtGui import QFont

    class Example(QWidget):
        def __init__(self):
            super().__init__(flags=Qt.WindowFlags())

            self.initUI()

        def initUI(self):
            QToolTip.setFont(QFont('SansSerif', 10))  # 设置全局tooltip的字体和大小
            self.setToolTip('This is a <b>QWidget</b> widget')  # 为窗口设置tooltip 好像无效
            btn = QPushButton('Button', self)  # 创建一个按钮，并与窗口进行绑定
            btn.setToolTip('This is a <b>QPushButton</b> widget')  # 为按钮设置Button
            btn.resize(btn.sizeHint())  # 设置按钮的大小,使用推荐大小
            btn.move(50, 50)  # 设置按钮的位置，左上角距离窗口左上角的位置
            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Tooltips')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def quit_button():
    from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            quit_btn = QPushButton('Quit', self)
            quit_btn.clicked.connect(QApplication.instance().quit)  # 为按钮的点击事件绑定应用的退出函数
            quit_btn.resize(quit_btn.sizeHint())
            quit_btn.move(50, 50)

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Quit button')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def message_box():
    from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Message box')
            self.show()

        def closeEvent(self, event):
            """
            右上角关闭触发事件
            """

            # 创建确认窗口，默认点击NO
            reply = QMessageBox.question(self, 'Message',
                                         "Are you sure to quit?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def center_desktop():
    """
    将窗口放在桌面中心
    :return:
    """
    from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.resize(250, 150)
            self.center()

            self.setWindowTitle('Center')
            self.show()

        def center(self):
            qr = self.frameGeometry()  # 获取到主窗口的外形
            cp = QDesktopWidget().availableGeometry().center()  # 获取到桌面的中心点
            qr.moveCenter(cp)  # 将主窗口的外形放在中心点
            self.move(qr.topLeft())  # 设置窗口的左上角为外形的左上角

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# simple()
# icon()
# tooltip()
# quit_button()
# message_box()
center_desktop()
