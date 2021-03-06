"""
消息对话框
"""

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('早点毕业吧--消息对话框')

        self.la = QLabel('这里将会显示我们选择的按钮信息', self)
        self.la.move(20, 20)
        self.bt1 = QPushButton('提示', self)
        self.bt1.move(20, 70)
        self.bt2 = QPushButton('询问', self)
        self.bt2.move(120, 70)
        self.bt3 = QPushButton('警告', self)
        self.bt3.move(220, 70)
        self.bt4 = QPushButton('错误', self)
        self.bt4.move(20, 140)
        self.bt5 = QPushButton('关于', self)
        self.bt5.move(120, 140)
        self.bt6 = QPushButton('关于Qt', self)
        self.bt6.move(220, 140)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()

    def info(self):
        reply = QMessageBox.information(self, '提示', '这是一个消息提示对话框!', QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.la.setText('你选择了Ok！')
        else:
            self.la.setText('你选择了Close！')

    def question(self):
        reply = QMessageBox.question(self, '询问', '这是一个询问消息对话框，默认是No',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.la.setText('你选择了Yes！')
        elif reply == QMessageBox.No:
            self.la.setText('你选择了No！')
        else:
            self.la.setText('你选择了Cancel！')

    def warning(self):
        cb = QCheckBox('所有文档都按此操作')  # 因为要在对话框中增加一个复选框，所以我新建了一个复选框对象，复选框的内容就是“所有文档都按此操作”
        msgBox = QMessageBox()
        msgBox.setWindowTitle('警告')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText('这是一个警告消息对话框')
        msgBox.setInformativeText('出现更改愿意保存吗?')
        Save = msgBox.addButton('保存', QMessageBox.AcceptRole)
        NoSave = msgBox.addButton('取消', QMessageBox.RejectRole)
        Cancel = msgBox.addButton('不保存', QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(Save)  # 设置了默认的按钮是保存
        msgBox.setCheckBox(cb)
        cb.stateChanged.connect(self.check)
        reply = msgBox.exec()#让消息对话框能够显示出来，并将我们选中的按钮返回给reply这个变量
        if reply == QMessageBox.AcceptRole:
            self.la.setText('你选择了保存！')
        elif reply == QMessageBox.RejectRole:
            self.la.setText('你选择了取消！')
        else:
            self.la.setText('你选择了不保存！')

    def critical(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')  # 该属性保存要在详细信息区域中显示的文本。文本将被解释为纯文本。默认情况下，此属性包含一个空字符串
        reply = msgBox.exec()

        if reply == QMessageBox.Retry:
            self.la.setText('你选择了Retry！')
        elif reply == QMessageBox.Abort:
            self.la.setText('你选择了Abort！')
        else:
            self.la.setText('你选择了Ignore！')

    def about(self):
        # QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', '不要意淫了，早点洗洗睡吧!')
        msgBox.setIconPixmap(QPixmap("beauty.png"))
        msgBox.exec()

    def aboutqt(self):
        QMessageBox.aboutQt(self, '关于Qt')

    def check(self):
        if self.sender().isChecked():
            self.la.setText('你打勾了哦')
        else:
            self.la.setText('怎么又不打了啊')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())