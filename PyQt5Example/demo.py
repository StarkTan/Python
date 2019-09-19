import sys
import imp
import utils
import os
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
        self.init_events()
        # 开启状态条
        self.status_bar = self.statusBar()
        self.serial_conn = None
        self.testcase_names = []
        self.test_modules = []
        self.test_record = []
        self.test_log = None
        self.initUI()

    def init_events(self):
        self.custom_single.serial_config[tuple].connect(self.serial_conn)
        self.custom_single.testcase_begin[int].connect(self.testcase_begin)
        self.custom_single.testcase_end[tuple].connect(self.testcase_end)
        self.custom_single.test_end.connect(self.test_end)
        self.custom_single.test_log[str].connect(self.add_log)

    def add_log(self, log_msg):
        self.test_log.add_logging(log_msg)

    def test_begin(self, config_data):
        self.test_log = TestLog()
        self.test_log.test_name = self.windowTitle()  # 测试项目名称
        self.test_log.test_auth = config_data[0]  # 测试人员
        self.test_log.serial_num = config_data[1]  # 产品序列号
        self.test_log.add_step("Begin")  # 设置日志位置

        self.add_log('开始测试！')
        self.test_record.clear()
        self.test_record.append(self.windowTitle())  # 项目名
        self.test_record.append(config_data[1])  # 产品序列号
        self.test_record.append(config_data[0])  # 操作人员
        self.test_record.append('测试通过')  # 测试结果
        self.test_record.append(QTime().currentTime().toString(Qt.DefaultLocaleLongDate))  # 测试时间

        btn = self.findChild(QPushButton, 'begin_btn')
        btn.setDisabled(True)
        testcase_table = self.findChild(TestCaseTable, 'testcase_table')
        testcase_table.init_data()

        workThread = WorkThread(self.custom_single, self.test_modules)
        workThread.start()

    def testcase_begin(self, data):
        print('第 %d 个测试用例开始' % data)
        self.test_log.add_step(self.testcase_names[data])  # 设置日志位置
        self.add_log('用例测试开始！')

        testcase_table = self.findChild(TestCaseTable, 'testcase_table')
        status = testcase_table.model.item(data, 1)
        check_btn = self.findChild(QPushButton, 'check_btn'+str(data))
        status.setText('开始测试')
        check_btn.setDisabled(False)
        begin_time_item = testcase_table.model.item(data, 3)
        begin_time_item.setText(QTime().currentTime().toString(Qt.DefaultLocaleLongDate))

    def testcase_end(self, data):
        print('第 %d 个测试用例结束' % data[0])

        testcase_table = self.findChild(TestCaseTable, 'testcase_table')
        status = testcase_table.model.item(data[0], 1)
        if data[1]:
            self.add_log('测试通过')
            status.setText('测试通过')
            status.setBackground(QColor('Green'))
            self.test_record.append('测试通过')
        else:
            self.add_log('测试失败')
            status.setText('测试失败')
            status.setBackground(QColor('Red'))
            self.test_record.append('测试失败')
            if not self.test_record[3] == '测试失败':
                self.test_record[3] = '测试失败'
        end_time_item = testcase_table.model.item(data[0], 4)
        end_time_item.setText(QTime().currentTime().toString(Qt.DefaultLocaleLongDate))
        self.add_log('用例测试完成！')

    def test_end(self):
        print('测试完成！')
        btn = self.findChild(QPushButton, 'begin_btn')
        btn.setDisabled(False)
        # 增加数据到结果列表
        self.tboard.tab2.add_record(self.test_record)
        self.test_log.add_step("End")  # 设置日志位置
        self.add_log('测试完成！')

    def initUI(self):
        # 初始化状态条展示
        self.status_bar.showMessage('Ready')
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)  # 中心窗口
        # 设置窗口外形
        self.resize(1200, 600)
        # 配置窗口大小固定不变
        self.setMinimumSize(1200, 600)  # 设置窗口最小限制
        self.setMaximumSize(1200, 600)  # 设置窗口最大限制
        self.setFixedSize(1200, 600)  # 配置窗口的无法最大化
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
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', 'Binary File(*.xml)')
        if len(fname[0]) > 0:
            self.test_modules.clear()
            res = utils.config_parse(fname[0])
            self.setWindowTitle(res['project'])
            # 加载测试的文件
            folder = os.path.split(fname[0])[0]
            for testcase in res['files']:
                file_path = os.path.join(folder, testcase+'.py')
                if os.path.exists(file_path):
                    fn_, path, desc = imp.find_module(testcase, [folder])
                    mod = imp.load_module(testcase, fn_, path, desc)
                    self.test_modules.append(mod)
                else:
                    print('load testcase error')

            self.testcase_names = res['files']
            # 展示测试项
            self.tboard.tab1.table.testcases = res['files']
            self.tboard.tab1.table.load_data()
            # 加载测试结果表头
            self.tboard.tab2.init_header(res['files'])

    def serial_conn_window(self):
        serial_config = SerialConfigWindow(self.custom_single)
        serial_config.exec_()

    def serial_conn(self, data):
        self.serial_conn = ''
        self.disconn_act.setDisabled(False)
        self.conn_act.setDisabled(True)

    def serial_disconn(self):
        self.serial_conn = None
        self.disconn_act.setDisabled(True)
        self.conn_act.setDisabled(False)

    def check_log(self, test_case_name):
        """
        展示对应测试用例的日志
        """
        records = self.test_log.testcases_logs[test_case_name]
        log_text = ''.join(records)

        log_window = LogWindow()
        log_window.setWindowTitle(test_case_name)
        log_window.log_edit.setText(log_text)
        log_window.exec_()


class CustomSingle(QObject):
    serial_config = pyqtSignal(tuple)
    testcase_begin = pyqtSignal(int)
    testcase_end = pyqtSignal(tuple)
    test_end = pyqtSignal()
    test_log = pyqtSignal(str)


class LogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 400)
        self.setWindowTitle('日志展示')
        self.setWindowModality(Qt.ApplicationModal)
        self.log_edit = QTextEdit()
        self.log_edit.setReadOnly(True)
        vbox = QVBoxLayout()
        vbox.addWidget(self.log_edit)

        self.setLayout(vbox)



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
        self.resize(1200, 600)

        left_widget = QListWidget()
        for name in ['测试用例', '测试记录']:
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
        self.tab2 = TestRecordTable()
        right_widget.addWidget(self.tab1)
        right_widget.addWidget(self.tab2)
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
        # hbox_main.addStretch(1)  # 添加一个伸缩量，可以看做左边填满


        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox_logo)
        vbox.addLayout(hbox_main)
        self.setLayout(vbox)


class TestCase(QWidget):
    """
    测试用例页面
    """
    def __init__(self, parent=None):
        super(TestCase, self).__init__(parent)
        layout = QVBoxLayout()

        self.table = TestCaseTable()
        self.table.setObjectName('testcase_table')
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

        self.testcases = []

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["用例名称", '状态', '日志', '开始时间', '结束时间', ''])

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
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        # 设置只能选中一行
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(2, 40)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)


    def load_data(self):
        self.model.removeRows(0, self.model.rowCount())
        for i in range(len(self.testcases)):
            testcase = self.testcases[i]
            item_name = QStandardItem(testcase)
            self.model.setItem(i, 0, item_name)
            item_status = QStandardItem('等待测试')
            self.model.setItem(i, 1, item_status)
            self.model.setItem(i, 3, QStandardItem(''))
            self.model.setItem(i, 4, QStandardItem(''))

    def init_data(self):
        row_count = self.model.rowCount()
        for i in range(row_count):
            status = self.model.item(i, 1)
            check_btn = self.findChild(QPushButton, 'check_btn' + str(i))
            status.setText('等待测试')
            status.setBackground(QColor('White'))
            check_btn.setDisabled(True)
            begin_time_item = self.model.item(i, 3)
            end_time_item = self.model.item(i, 4)
            begin_time_item.setText('')
            end_time_item.setText('')

    def check_log(self):
        index = self.tableView.currentIndex()
        test_case_name = self.model.item(index.row(), 0).text()
        self.parent().parent().parent().parent().check_log(test_case_name)


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
            button.setObjectName('check_btn'+str(index.row()))
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
        self.begin_btn.setObjectName('begin_btn')
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
        if data1 == '' or data2 == '' or data3 == '':
            QMessageBox.warning(self, '错误', '消息输入不完成！', QMessageBox.Close, QMessageBox.Close)
            return
        data4 = self.edit4.text()
        data5 = self.edit5.text()
        data6 = self.edit6.text()
        self.parent().parent().parent()\
            .parent().test_begin((data1, data2, data3, data4, data5, data6))


class TestRecordTable(QWidget):
    """
    测试记录
    """
    def __init__(self, parent=None):
        super(TestRecordTable, self).__init__(parent)
        self.init_data()
        self.show_data()

    def init_data(self):
        self.headers = ['项目名称', '产品序列号', '测试人员', '测试结果', '测试时间']
        self.datas = [
            ['项目一', '000001', '073130', '2019-01-01 14:00:00', 'PASS', 'PASS', "PASS", 'PASS', 'PASS'],
            ['项目一', '000002', '073130', '2019-01-01 14:05:00', 'FAILED', 'PASS', "PASS", 'PASS', 'FAILED'],
            ['项目一', '000003', '073130', '2019-01-01 14:10:00', 'FAILED', 'PASS', "PASS", 'FAILED', 'PASS']
        ]

    def show_data(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.headers)
        # for row in range(len(self.datas)):
        #     data = self.datas[row]
        #     for column in range(len(self.headers)):
        #         item = QStandardItem(data[column])
        #         if data[column] == 'PASS':
        #             item.setForeground(QBrush(QColor(0, 255, 0)))
        #         if data[column] == 'FAILED':
        #             item.setForeground(QBrush(QColor(255, 0, 0)))
        #         self.model.setItem(row, column, item)
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(0)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

    def init_header(self, headers):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(self.headers+headers+[''])

    def add_record(self, datas):
        row = self.model.rowCount()
        for i in range(len(datas)):
            data = datas[i]
            item = QStandardItem(data)
            if data == '测试失败':
                item.setBackground(QColor('Red'))
            if data == '测试通过':
                item.setBackground(QColor('Green'))
            self.model.setItem(row, i, item)


class WorkThread(QThread):
    def __init__(self, custom_single, modules):
        super(WorkThread, self).__init__()
        self.custom_single = custom_single
        self.modules = modules

    def run(self):
        modules = self.modules
        for i in range(len(modules)):
            self.custom_single.testcase_begin.emit(i)
            module = modules[i]
            test_case = module.TestCase(serial=None, logger=self.logger)
            res = test_case.test()
            self.custom_single.testcase_end.emit((i, res))
        self.custom_single.test_end.emit()

    def logger(self, msg):
        self.custom_single.test_log.emit(msg)


class TestLog(object):
    """
    每一次项目测试的日志
    """
    def __init__(self):
        self.test_name = ''  # 测试项目名称
        self.test_auth = ''  # 测试人员
        self.serial_num = ''  # 产品序列号
        self.testcases = []  # 测试用例名，用于排序
        self.testcases_logs = {}  # 测试用例执行中的日志

        self.current_logs = None  # 当前测试需要的日志

    def add_step(self, name):
        """
        设置当前测试项
        """
        self.testcases.append(name)
        self.testcases_logs[name] = []
        self.current_logs = self.testcases_logs[name]

    def add_logging(self, log):
        current_time = QDateTime().currentDateTime().toString(Qt.ISODate)
        self.current_logs.append('%s : %s \n' % (current_time, log))

    def create_file(self, dir_path):
        """
        创建日志文件
        """
        return

    def load_file(self, file_path):
        """
        加载日志文件
        """
        return


app = QApplication([])
demo = Demo()
demo.show()
sys.exit(app.exec_())
