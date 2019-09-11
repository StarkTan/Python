"""
PyQt5 部分高级的组件
"""

import sys


def tab_widget():

    from PyQt5.QtWidgets import (QTabWidget, QWidget, QFormLayout, QLabel, QCheckBox,
                                 QLineEdit, QHBoxLayout, QRadioButton, QApplication)

    class TabDemo(QTabWidget):
        def __init__(self, parent=None):
            super(TabDemo, self).__init__(parent)
            self.setGeometry(300, 300, 280, 170)
            # 创建3个选项卡小控件窗口
            self.tab1 = QWidget()
            self.tab2 = QWidget()
            self.tab3 = QWidget()

            # 将三个选项卡添加到顶层窗口中
            self.addTab(self.tab1, "Tab 1")
            self.addTab(self.tab2, "Tab 2")
            self.addTab(self.tab3, "Tab 3")

            # 每个选项卡自定义的内容
            self.tab1UI()
            self.tab2UI()
            self.tab3UI()

        def tab1UI(self):
            # 表单布局
            layout = QFormLayout()
            # 添加姓名，地址的单行文本输入框
            layout.addRow('姓名', QLineEdit())
            layout.addRow('地址', QLineEdit())
            # 设置选项卡的小标题与布局方式
            self.setTabText(0, '联系方式')
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

            # 设置标题与布局
            self.setTabText(1, '个人详细信息')
            self.tab2.setLayout(layout)

        def tab3UI(self):
            # 水平布局
            layout = QHBoxLayout()

            # 添加控件到布局中
            layout.addWidget(QLabel('科目'))
            layout.addWidget(QCheckBox('物理'))
            layout.addWidget(QCheckBox('高数'))

            # 设置小标题与布局方式
            self.setTabText(2, '教育程度')
            self.tab3.setLayout(layout)

    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())


def left_tab_widget():
    from PyQt5.QtWidgets import (QListWidget, QWidget, QFormLayout, QLabel, QCheckBox,
                                 QLineEdit, QHBoxLayout, QRadioButton, QApplication,
                                 QStackedWidget,QListWidgetItem,)
    from PyQt5.QtCore import Qt,QSize

    class LeftTabWidget(QWidget):
        def __init__(self):
            super(LeftTabWidget, self).__init__()
            self.setWindowTitle('LeftTabWidget')

            # 创建 QListWidget
            left_widget = QListWidget()
            for name in ['联系方式', '个人详细信息', '教育程度']:
                item = QListWidgetItem(name, left_widget)
                item.setSizeHint(QSize(30, 30))
                item.setTextAlignment(Qt.AlignCenter)

            # 设置样式
            list_style = """QListWidget, QListView, QTreeWidget, QTreeView {
                        outline: 0px;
                        }
                        
                        QListWidget {
                        min-width: 120px;
                        max-width: 120px;
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
            self.tab1 = QWidget()
            self.tab2 = QWidget()
            self.tab3 = QWidget()
            self.tab1UI()
            self.tab2UI()
            self.tab3UI()
            right_widget.addWidget(self.tab1)
            right_widget.addWidget(self.tab2)
            right_widget.addWidget(self.tab3)
            left_widget.currentRowChanged.connect(right_widget.setCurrentIndex)

            hbox = QHBoxLayout()
            hbox.addStretch(1)  # 添加一个伸缩量，可以看做左边填满
            hbox.addWidget(left_widget)
            hbox.addWidget(right_widget)

            self.setLayout(hbox)

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

            # 设置小标题与布局方式
            self.tab3.setLayout(layout)

    app = QApplication(sys.argv)
    demo = LeftTabWidget()
    demo.show()
    sys.exit(app.exec_())


# tab_widget()
left_tab_widget()

