"""
PyQt5 中使用到的菜单栏和工具栏
"""

import sys


def status_bar():
    """
    状态条：右下角的展示消息
    """
    from PyQt5.QtWidgets import QMainWindow, QApplication

    class Example(QMainWindow):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            # 获取 状态条 添加展示信息
            self.statusBar().showMessage('Ready')

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Statusbar')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def simple_menu():
    """
    创建简单的菜单
    """
    from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
    from PyQt5.QtGui import QIcon

    class Example(QMainWindow):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.statusBar()  # 创建状态条

            exitAct = QAction(QIcon('exit.jpg'), '&Exit', self)  # 创建菜单选项
            exitAct.setShortcut('Ctrl+Q')  # 添加快捷键
            exitAct.setStatusTip('Exit application')  # 在状态条中展示提示信息
            exitAct.triggered.connect(qApp.quit)  # 绑定选中事件

            menubar = self.menuBar()  # 创建菜单栏
            fileMenu = menubar.addMenu('&File')  # 添加菜单
            fileMenu.addAction(exitAct)  # 添加菜单栏选项

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Simple menu')
            self.show()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def sub_menu():
    """
    创建子菜单
    """
    from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

    class Example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            menubar = self.menuBar()
            fileMenu = menubar.addMenu('File')

            impMenu = QMenu('Import', self)  # 创建子菜单
            impAct = QAction('Import mail', self)
            impMenu.addAction(impAct)

            newAct = QAction('New', self)
            # 在File菜单中加入选项和子菜单
            fileMenu.addAction(newAct)
            fileMenu.addMenu(impMenu)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Submenu')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def check_menu():
    """
    可勾选菜单栏
    """
    from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

    class Example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 状态条展示Ready
            self.statusbar = self.statusBar()
            self.statusbar.showMessage('Ready')

            # 菜单栏添加 View 菜单
            menubar = self.menuBar()
            viewMenu = menubar.addMenu('View')

            # 创建可勾选选项
            viewStatAct = QAction('View statusbar', self, checkable=True)
            viewStatAct.setStatusTip('View statusbar')  # 配置提示信息
            viewStatAct.setChecked(True)  # 设置默认勾选
            viewStatAct.triggered.connect(self.toggleMenu)  # 为选项绑定事件函数

            viewMenu.addAction(viewStatAct)  #

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Check menu')
            self.show()

        def toggleMenu(self, state):
            """
            根据状态判断是否展示状态条
            """
            if state:
                self.statusbar.show()
            else:
                self.statusbar.hide()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def context_menu():
    """
    弹出菜单
    """
    from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

    class Example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Context menu')
            self.show()

        def contextMenuEvent(self, event):
            """
            重写 contextMenuEvent 事件
            """
            # 创建菜单并绑定选项
            cmenu = QMenu(self)
            newAct = cmenu.addAction("New")
            opnAct = cmenu.addAction("Open")
            quitAct = cmenu.addAction("Quit")
            # 使菜单展示在鼠标右击的位置
            action = cmenu.exec_(self.mapToGlobal(event.pos()))

            if action == quitAct:
                qApp.quit()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def toolbar():
    """
    工具条
    """
    from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
    from PyQt5.QtGui import QIcon

    class Example(QMainWindow):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            # 创建退出选项
            exitAct = QAction(QIcon('exit.jpg'), 'Exit', self)
            exitAct.setShortcut('Ctrl+Q')
            exitAct.triggered.connect(qApp.quit)
            # 创建工具条，创建多个工具条是一排并列的
            self.toolbar = self.addToolBar('One')
            self.toolbar.addAction(exitAct)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Toolbar')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def mainwindow():
    """
    将菜单栏和工具条放在一起
    """
    from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
    from PyQt5.QtGui import QIcon

    class Example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 将文字居中
            textEdit = QTextEdit()
            self.setCentralWidget(textEdit)

            # 创建选项
            exitAct = QAction(QIcon('exit.jpg'), 'Exit', self)
            exitAct.setShortcut('Ctrl+Q')
            exitAct.setStatusTip('Exit application')
            exitAct.triggered.connect(self.close)
            # 创建状态条
            self.statusBar()
            # 创建菜单栏和菜单，添加选项
            menubar = self.menuBar()
            fileMenu = menubar.addMenu('&File')
            fileMenu.addAction(exitAct)
            # 创建工具条，添加选项
            toolbar = self.addToolBar('Exit')
            toolbar.addAction(exitAct)

            self.setGeometry(300, 300, 350, 250)
            self.setWindowTitle('Main window')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# status_bar()
# simple_menu()
# sub_menu()
# check_menu()
# context_menu()
# toolbar()
mainwindow()
