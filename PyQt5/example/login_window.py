from PyQt5.Qt import *
import sys
import math


class AccountTool:  # 帐户判定类
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3

    @staticmethod  # 定义静态方法
    def check_login(account, pwd):
        # 把帐号和密码发送给服务器，等待服务器返回结果
        if account != "kaixinde101":
            return AccountTool.ACCOUNT_ERROR
        elif pwd != "12345678":
            return AccountTool.PWD_ERROR
        else:
            return AccountTool.SUCCESS


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登陆界面")
        self.setWindowIcon(QIcon("../pyqt.jpg"))
        self.resize(500, 200)
        # self.Password="12345678"
        # self.UserName="kaixinde101"
        self.Co_Width = 40
        self.Co_Heigth = 20
        self.setMinimumSize(500, 200)  # 设置最小尺寸500*200
        self.setMaximumSize(500, 200)  # 设置最大尺寸500*200
        self.setup_ui()

    def setup_ui(self):
        self.lab_l = QLabel("帐户:", self)  # 帐户标签
        self.Lin_l = QLineEdit(self)  # 帐户录入框
        self.lab_Account_ERROR = QLabel(self)  # 帐户录入报错标签
        self.lab_p = QLabel("密码:", self)  # 密码标签
        self.Lin_p = QLineEdit(self)  # 密码录入框
        self.Lin_p.setEchoMode(QLineEdit.Password)  # 设置密文显示
        self.lab_Password_ERROR = QLabel(self)  # 密码录入报错标签
        self.Pu_l = QPushButton(QIcon("../pyqt.jpg"), "登陆&L", self)  # 登陆按钮
        self.Login_Success = QLabel(self)  # 登陆结果
        self.Pu_l.clicked.connect(self.Login)
        self.Lin_l.textChanged.connect(self.Cls_Err_Show)  # 帐户登内容改变
        self.Lin_p.textChanged.connect(self.Cls_Err_Show)  # 密码登内容改变
        self.Lin_l.setPlaceholderText("请输入账号")  # 占位文本设置
        self.Lin_p.setPlaceholderText("请输入密码")  # 占位文本设置
        self.Lin_p.setClearButtonEnabled(True)  # 设置清空按钮
        # 添加自定义行为操作（明文和密文的切换）
        action = QAction(self.Lin_p)
        action.setIcon(QIcon("../pyqt.jpg"))

        # 改变密码显示方式
        def change():
            if (self.Lin_p.echoMode() == QLineEdit.Normal):  # 明文切换成密文
                self.Lin_p.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon("../pyqt.jpg"))
            elif (self.Lin_p.echoMode() == QLineEdit.Password):  # 密文切换成明文
                self.Lin_p.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon("../pyqt.jpg"))

        action.triggered.connect(change)
        self.Lin_p.addAction(action, QLineEdit.TrailingPosition)  # 图标在QLineEdit控件中的位置

        # 自动补全联想帐号
        completer = QCompleter(["kaixinde101", "kaixinde", "shenbo", "shenbo200809"], self.Lin_l)  # 提供可参考的原组
        self.Lin_l.setCompleter(completer)

        # QLinEdit-文本内容限制-长度和只读限制
        self.Lin_l.setMaxLength(13)  # 设置帐户最大长度为13
        self.Lin_p.setReadOnly(False)  # 设置为只读

        # QLineEdit-文本内容限制-验证器使用

        # self.lab_l.keyPressEvent()
        # self.Lin_l.keyPressEvent(lambda:self.Lin_p.setFocus())#键盘按下切换焦点

    def resizeEvent(self, evt):  # 重新设置控件座标事件
        # 帐户标签
        self.lab_l.resize(self.Co_Width, self.Co_Heigth)
        self.lab_l.move(self.width() / 3, self.height() / 5)
        # 帐户录入框
        self.Lin_l.move(self.lab_l.x() + self.lab_l.width(), self.lab_l.y())
        # 帐户报错提示框
        self.lab_Account_ERROR.resize(100, 20)
        self.lab_Account_ERROR.move(self.Lin_l.x(), self.Lin_l.y() + self.Lin_l.height() / 1.3)
        # 密码标签
        self.lab_p.resize(self.Co_Width, self.Co_Heigth)
        self.lab_p.move(self.lab_l.x(), self.lab_l.y() + self.lab_l.height() * 2.2)
        # 密码录入框
        self.Lin_p.move(self.lab_p.x() + self.lab_p.width(), self.lab_p.y())
        # 密码报错提示框
        self.lab_Password_ERROR.resize(100, 20)
        self.lab_Password_ERROR.move(self.Lin_p.x(), self.Lin_p.y() + self.Lin_p.height() / 1.3)
        # 登陆按钮
        self.Pu_l.move(self.Lin_p.x() + self.Lin_p.width() / 4, self.lab_p.y() + self.lab_p.height() * 2.2)
        # 登陆结果
        self.Login_Success.resize(100, 20)
        self.Login_Success.move(self.Lin_p.x(), self.Pu_l.y() + self.Pu_l.height())

    def Login(self):
        state = AccountTool.check_login(self.Lin_l.text(), self.Lin_p.text())
        if state == AccountTool.ACCOUNT_ERROR:
            self.Lin_l.setText("")
            self.Lin_p.setText("")
            self.Lin_l.setFocus()  # 设置焦点
            # self.lab_Account_ERROR.setStyleSheet("background-color:red;")#设置背景颜色为红色
            self.lab_Account_ERROR.setStyleSheet("color:red;")  # 设置字体颜色为红色
            self.lab_Account_ERROR.setText("帐户录入错误!!")
            # print("帐户录入错误!!")
        elif state == AccountTool.PWD_ERROR:
            self.Lin_p.setText("")
            # self.lab_Password_ERROR.setStyleSheet("background-color:red;")#设置背景颜色为红色
            self.lab_Password_ERROR.setStyleSheet("color:red;")  # 设置字体颜色为红色
            self.lab_Password_ERROR.setText("密码录入错误!!")
            # print("密码录入错误!!")
            self.Lin_p.setFocus()  # 设置焦点
        elif state == AccountTool.SUCCESS:
            # self.Login_Success.setStyleSheet("background-color:green;")#设置背景颜色为绿色
            self.Login_Success.setStyleSheet("color:green;")  # 设置字体颜色为绿色
            self.Login_Success.setText("登陆成功!!")
            # print("登陆成功!!")

    def Cls_Err_Show(self):
        self.lab_Account_ERROR.setText("")
        self.lab_Password_ERROR.setText("")
        self.Login_Success.setText("")
        # self.lab_Password_ERROR.setStyleSheet("background-color:white;")#设置密码提示框背景颜色为白色
        # self.lab_Account_ERROR.setStyleSheet("background-color:white;")#设置帐户提示框背景颜色为白色
        # self.Login_Success.setStyleSheet("background-color:white;")#设置登陆提示框背景颜色为白色


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Win = Window()
    Win.show()
    sys.exit(App.exec_())
