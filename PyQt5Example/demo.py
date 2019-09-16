import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Demo(QMainWindow):
    """
    QMainWindow 类提供了一个主应用程序窗口
    """
    def __init__(self):
        super().__init__()
        # 创建自定义事件通知器
        self.custom_single = CustomSingle()
        self.custom_single.serial_config[tuple].connect(self.serial_conn)
        # 开启状态条
        self.status_bar = self.statusBar()
        self.serial_conn = None

        self.initUI()

    def initUI(self):
        # 初始化状态条展示
        self.status_bar.showMessage('Ready')
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)  # 中心窗口
        # 设置窗口外形
        self.resize(1000, 500)
        # 配置窗口大小固定不变
        self.setMinimumSize(1000, 500)  # 设置窗口最小限制
        self.setMaximumSize(1000, 500)  # 设置窗口最大限制
        self.setFixedSize(1000, 500)  # 配置窗口的无法最大化
        # 设置窗口展示
        self.setWindowIcon(QIcon('resources/pyqt.jpg'))  # 设置串口图标
        self.center()  # 配置窗口桌面居中
        self.setWindowTitle('Demo')  # 设置窗口名
        self.init_menu()

    def center(self):
        """窗口居中"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def init_menu(self):
        """创建菜单栏"""


        choice_project = QAction(QIcon(''), '&配置项目', self)
        choice_project.setShortcut('Ctrl+O')
        choice_project.setStatusTip('选择测试项目')
        choice_project.triggered.connect(self.load_project)

        conn_act = QAction(QIcon(''), '&连接串口', self)
        conn_act.setShortcut('Ctrl+N')
        conn_act.setStatusTip('创建串口连接')
        conn_act.triggered.connect(self.serial_conn_window)

        disconn_act = QAction(QIcon(''), '&断开连接', self)
        disconn_act.setShortcut('Ctrl+I')
        disconn_act.setStatusTip('断开串口连接')
        disconn_act.triggered.connect(self.serial_disconn)
        disconn_act.setDisabled(True)

        self.conn_act = conn_act
        self.disconn_act = disconn_act
        # 创建菜单栏和菜单，添加选项
        menubar = self.menuBar()
        config_menu = menubar.addMenu('&配置')
        config_menu.addAction(choice_project)
        config_menu.addAction(conn_act)
        config_menu.addAction(disconn_act)

    def load_project(self):
        # 打开文件选择框
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(fname)

    def serial_conn_window(self):
        serial_config = SerialConfigWindow(self.custom_single)
        serial_config.exec_()

    def serial_conn(self, data):
        print(data)
        self.serial_conn = ''
        self.disconn_act.setDisabled(False)
        self.conn_act.setDisabled(True)

    def serial_disconn(self):
        self.serial_conn = None
        self.disconn_act.setDisabled(True)
        self.conn_act.setDisabled(False)


class CustomSingle(QObject):
    serial_config = pyqtSignal(tuple)


class SerialConfigWindow(QDialog):
    """
    QMainWindow 类提供了一个主应用程序窗口
    """
    def __init__(self, custom_single):
        super().__init__()
        self.custom_single = custom_single
        self.init_ui()

    def init_ui(self):
        self.resize(250, 100)
        self.setWindowTitle('串口连接')
        self.setWindowModality(Qt.ApplicationModal)

        port_combo = QComboBox(self)
        port_combo.resize(20, 10)
        port_combo.addItem("COM1")
        port_combo.addItem("COM2")
        port_combo.addItem("COM3")
        port_combo.addItem("COM4")
        port_combo.addItem("COM5")

        baudrate_combo = QComboBox(self)
        baudrate_combo.addItem("9600")
        baudrate_combo.addItem("115200")
        baudrate_combo.addItem("460800")
        baudrate_combo.addItem("1000000")

        ok_btn = QPushButton('确定', self)
        ok_btn.clicked.connect(self.serial_conn)

        cancel_btn = QPushButton('取消', self)
        cancel_btn.clicked.connect(self.close)

        port_lbl = QLabel("串口：", self)
        baudrate_lbl = QLabel("波特率：", self)


        self.port_combo = port_combo
        self.baudrate_combo = baudrate_combo

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(port_lbl)
        hbox1.addWidget(port_combo)
        hbox1.addStretch(1)
        hbox1.addWidget(baudrate_lbl)
        hbox1.addWidget(baudrate_combo)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(ok_btn)
        hbox2.addStretch(1)
        hbox2.addWidget(cancel_btn)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

    def serial_conn(self):
        port = str(self.port_combo.currentText())
        baudrate = int(self.baudrate_combo.currentText())

        self.custom_single.serial_config.emit((port, baudrate))
        self.close()


class Board(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_board()

    def init_board(self):
        # 创建 QListWidget
        self.resize(1000, 500)

        left_widget = QListWidget()
        for name in ['测试用例', '测试报告',"测试日志"]:
            item = QListWidgetItem(name, left_widget)
            item.setSizeHint(QSize(60, 80))
            item.setTextAlignment(Qt.AlignCenter)
            if name == '测试用例':
                item.setSelected(True)

        # 设置样式
        list_style = """QListWidget, QListView, QTreeWidget, QTreeView {
                                outline: 0px;
                                }

                                QListWidget {
                                min-width: 200px;
                                max-width: 200px;
                                color: Black;
                                background: #F5F5F5;
                                }

                                QListWidget::Item:selected {
                                background: lightGray;
                                border-left: 5px solid red;
                                }

                                HistoryPanel:hover {
                                background: rgb(52, 52, 52);
                                }"""
        left_widget.setStyleSheet(list_style)
        left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框
        left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        right_widget = QStackedWidget()
        self.tab1 = TestCase()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab2UI()
        self.tab3UI()
        right_widget.addWidget(self.tab1)
        right_widget.addWidget(self.tab2)
        right_widget.addWidget(self.tab3)
        left_widget.currentRowChanged.connect(right_widget.setCurrentIndex)

        project_logo = QLabel(self)
        project_logo.setPixmap(QPixmap("resources/项目.PNG"))

        company_logo = QLabel(self)
        company_logo.setPixmap(QPixmap("resources/公司.PNG"))

        hbox_logo = QHBoxLayout()
        hbox_logo.addWidget(project_logo)
        hbox_logo.addStretch(1)
        hbox_logo.addWidget(company_logo)

        hbox_main = QHBoxLayout()
        hbox_main.addWidget(left_widget)
        hbox_main.addWidget(right_widget)
        hbox_main.addStretch(1)  # 添加一个伸缩量，可以看做左边填满


        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox_logo)
        vbox.addLayout(hbox_main)
        self.setLayout(vbox)

    def tab1UI(self):
        # 表单布局
        layout = QFormLayout()
        # 添加姓名，地址的单行文本输入框
        layout.addRow('姓名', QLineEdit())
        layout.addRow('地址', QLineEdit())
        # 设置选项卡的小标题与布局方式
        self.tab1.setLayout(layout)

    def tab2UI(self):
        # zhu表单布局，次水平布局
        layout = QFormLayout()
        sex = QHBoxLayout()

        # 水平布局添加单选按钮
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))

        # 表单布局添加控件
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())

        self.tab2.setLayout(layout)

    def tab3UI(self):
        # 水平布局
        layout = QHBoxLayout()

        # 添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('高数'))

        # 设置小标题与布局方式
        self.tab3.setLayout(layout)


class TestCase(QWidget):
    """
    测试用例页面
    """
    def __init__(self, parent=None):
        super(TestCase, self).__init__(parent)
        layout = QVBoxLayout()

        self.table = TestCaseTable()
        self.config = TestCaseConfig()
        layout.addWidget(self.table)
        layout.addWidget(self.config)
        self.setLayout(layout)


class TestCaseTable(QWidget):
    """
    测试用例界面上部列表
    """
    def __init__(self, parent=None):
        super(TestCaseTable, self).__init__(parent)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["用例名称", '状态', '日志',' '])

        for row in range(20):
            name_item = QStandardItem('测试用例 %d' % row)
            self.model.setItem(row, 0, name_item)
            status = random.randint(1, 4)
            if status == 1:
                status_item = QStandardItem('Waiting')
                self.model.setItem(row, 1, status_item)
            elif status == 2:
                status_item = QStandardItem('Testing')
                self.model.setItem(row, 1, status_item)
            elif status == 3:
                status_item = QStandardItem('Passed')
                self.model.setItem(row, 1, status_item)
            else:
                status_item = QStandardItem('Failed')
                self.model.setItem(row, 1, status_item)
            # self.model.setItem(row, 2,  CheckLogButton(self.model))

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegateForColumn(2, CheckLogButton(self))

        # 水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，配置列的宽度修改方式
        self.tableView.horizontalHeader().setSectionResizeMode(0)
        # 设置不可编辑
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        # 设置行选中
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置只能选中一行
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(2, 40)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

    def check_log(self):
        """
        TODO 弹出当前测试日志的窗口
        """
        index = self.tableView.currentIndex()
        test_case = self.model.item(index.row(), 0).text()
        print(test_case)

class CheckLogButton(QItemDelegate):
    def __init__(self, parent=None):
        super(CheckLogButton, self).__init__(parent)

    def paint(self, painter, option, index):
        if not self.parent().tableView.indexWidget(index):
            button = QPushButton(
                self.tr('查看'),
                self.parent(),
                clicked = self.parent().check_log
            )
            if index.row() > 0:
                button.setDisabled(True)
            self.parent().tableView.setIndexWidget(
                index,
                button
            )


class TestCaseConfig(QWidget):
    """
    测试用例界面下方输入框
    """
    def __init__(self, parent=None):
        super(TestCaseConfig, self).__init__(parent)
        label1 = QLabel('工号')
        label2 = QLabel('序列号')
        label3 = QLabel('MaC地址1')
        label4 = QLabel('Mac地址2')
        label5 = QLabel('Input5')
        label6 = QLabel('Input6')

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()

        grid = QGridLayout()

        grid.addWidget(label1, 1, 0)
        grid.addWidget(self.edit1, 1, 1)
        grid.addWidget(label2, 1,2)
        grid.addWidget(self.edit2, 1, 3)

        grid.addWidget(label3, 2, 0)
        grid.addWidget(self.edit3, 2, 1)
        grid.addWidget(label4, 2, 2)
        grid.addWidget(self.edit4, 2, 3)
        self.edit4.setDisabled(True)
        self.edit3.textChanged[str].connect(lambda data : self.edit4.setText(data))

        grid.addWidget(label5, 3, 0)
        grid.addWidget(self.edit5, 3, 1)
        grid.addWidget(label6, 3, 2)
        grid.addWidget(self.edit6, 3, 3)
        self.edit5.setDisabled(True)
        self.edit6.setDisabled(True)


        self.begin_btn = QPushButton('开始')
        self.begin_btn.setMinimumSize(80, 60)
        self.begin_btn.setMaximumSize(80, 60)
        self.begin_btn.clicked.connect(self.begin_test)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.begin_btn)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addLayout(grid)
        hbox.addLayout(vbox)

        self.setLayout(hbox)


    def begin_test(self):
        data1 = self.edit1.text()
        data2 = self.edit2.text()
        data3 = self.edit3.text()
        data4 = self.edit4.text()
        data5 = self.edit5.text()
        data6 = self.edit6.text()

        print(data1,data2,data3,data4,data5,data6)


app = QApplication([])
demo = Demo()
demo.show()
sys.exit(app.exec_())
