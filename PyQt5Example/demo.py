import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class Demo(QMainWindow):
    """
    QMainWindow 类提供了一个主应用程序窗口
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 开启状态条
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        # 设置窗口外形
        self.resize(800, 500)
        # 配置窗口大小固定不变
        self.setMinimumSize(800, 500)  # 设置窗口最小限制
        self.setMaximumSize(800, 500)  # 设置窗口最大限制
        self.setFixedSize(800, 500)  # 配置窗口的无法最大化

        self.setWindowIcon(QIcon('resources/pyqt.jpg'))  # 设置串口图标

        self.center()  # 配置窗口桌面居中
        self.setWindowTitle('Demo')  # 设置窗口名
        self.show()

    def center(self):
        """窗口居中"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


app = QApplication([])
tetris = Demo()
sys.exit(app.exec_())