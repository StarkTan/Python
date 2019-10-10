"""
表单功能测试
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QFrame,
                             QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QIntValidator


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = None
        self.init_window()
        self.init_ui()

    def init_window(self):
        self.resize(300, 400)
        self.setMinimumSize(300, 400)
        self.setMaximumSize(300, 400)
        self.setFixedSize(300, 400)
        self.setWindowIcon(QIcon('../resources/pyqt.jpg'))
        self.setWindowTitle('Form 测试')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def init_ui(self):
        self.board = Form(self)
        self.setCentralWidget(self.board)


class Form(QFrame):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.labels = []
        self.edits = []
        self.confirm = None
        self.cancel = None
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.add_input()
        self.add_btns()

    def add_input(self):
        hhox = QHBoxLayout()
        label = QLabel("测试一：")
        edit = ValidLineEdit()
        edit.set_allow_blank(False)
        edit.setObjectName('测试一')
        hhox.addStretch(1)
        hhox.addWidget(label)
        hhox.addStretch(1)
        hhox.addWidget(edit)
        hhox.addStretch(1)
        self.vbox.addLayout(hhox)
        self.labels.append(label)
        self.edits.append(edit)

    def add_btns(self):
        self.confirm = QPushButton('确定')
        self.confirm.clicked.connect(self.commit)
        self.cancel = QPushButton('取消')
        self.cancel.clicked.connect(self.parent().close)
        hhox = QHBoxLayout()
        hhox.addStretch(1)
        hhox.addWidget(self.confirm)
        hhox.addStretch(1)
        hhox.addWidget(self.cancel)
        hhox.addStretch(1)
        self.vbox.addLayout(hhox)
        self.cancel = None

    def commit(self):
        data_ok = True
        for edit in self.edits:
            edit: ValidLineEdit
            data_ok = data_ok and edit.validate()


class ValidLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(ValidLineEdit, self).__init__(parent)
        self.set_ok_color()
        self.textChanged.connect(self.validate)

        self._allow_blank = True  # 数据可以为空
        self._max_len = None  # 最大长度
        self._min_len = None  # 最小长度
        self._error_msg = ''

    def set_max_len(self, max_len):
        if not isinstance(max_len, int):
            raise Exception('max_len 数据类型必须为整数')
        if not max_len > 0:
            raise Exception('输入最大长度必须大于 0 ')
        self._max_len = max_len
        self.setMaxLength(max_len)

    def max_len(self):
        return self._max_len

    def set_min_len(self, min_len):
        if not isinstance(min_len, int):
            raise Exception('max_len 数据类型必须为整数')
        if not min_len > 0:
            raise Exception('输入最大长度必须大于 0 ')
        self._min_len = min_len

    def min_len(self):
        return self._min_len

    def set_allow_blank(self, allow):
        if not isinstance(allow, bool):
            raise Exception('max_len 数据类型必须布尔')
        self._allow_blank = allow

    def allow_blank(self):
        return self._allow_blank

    def set_error_color(self):
        color_style = 'border: 1px solid #FF0000'
        self.setStyleSheet(color_style)

    def set_ok_color(self):
        color_style = 'border: 1px solid #0000FF'
        self.setStyleSheet(color_style)

    def validate(self):
        text = self.text()
        try:
            if not self._allow_blank and text == '':
                self._error_msg = '输入不允许为空'
                return False
            if self._min_len is not None and len(text) < self._min_len:
                self._error_msg = '输入最小长度为%s' % self._min_len
                return False
        finally:
            self.set_error_color()
        self.set_ok_color()
        return True


app = QApplication([])
demo = Window()
demo.show()
sys.exit(app.exec_())
