"""
使用 PyQt 进行简单绘图
"""
import sys


def drawing_text():
    """
    绘制文字
    """
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QPainter, QColor, QFont
    from PyQt5.QtCore import Qt

    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.text = "Лев Николаевич Толстой\nАнна Каренина"
            self.setGeometry(300, 300, 280, 170)
            self.setWindowTitle('Drawing text')
            self.show()

        def paintEvent(self, event):
            """
            在串口内容初始化时触发
            """
            qp = QPainter()
            qp.begin(self)  # 绘制开始
            self.drawText(event, qp)
            qp.end()  # 绘制结束

        def drawText(self, event, qp):
            # 配置颜色和字体
            qp.setPen(QColor(168, 34, 3))
            qp.setFont(QFont('Decorative', 10))
            # 绘制文字
            qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def points():
    """
    绘制点
    """
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QPainter
    from PyQt5.QtCore import Qt
    import random

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 300, 190)
            self.setWindowTitle('Points')
            self.show()

        def paintEvent(self, e):
            qp = QPainter()
            qp.begin(self)
            self.drawPoints(qp)
            qp.end()

        def drawPoints(self, qp):
            qp.setPen(Qt.red)
            size = self.size()

            for i in range(1000):
                x = random.randint(1, size.width() - 1)
                y = random.randint(1, size.height() - 1)
                qp.drawPoint(x, y)  # 绘制点

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def colours():
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QPainter, QColor, QBrush

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 350, 100)
            self.setWindowTitle('Colours')
            self.show()

        def paintEvent(self, e):
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

        def drawRectangles(self, qp):
            # 修改pen 去除边框
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)

            qp.setBrush(QColor(200, 0, 0))
            qp.drawRect(10, 15, 90, 60)  # 画长方形，使用的是Brush

            qp.setBrush(QColor(255, 80, 0, 160))
            qp.drawRect(130, 15, 90, 60)

            qp.setBrush(QColor(25, 0, 90, 200))
            qp.drawRect(250, 15, 90, 60)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def pens():
    """
    不同类型的线条
    """
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QPainter, QPen
    from PyQt5.QtCore import Qt

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 280, 270)
            self.setWindowTitle('Pen styles')
            self.show()

        def paintEvent(self, e):
            qp = QPainter()
            qp.begin(self)
            self.drawLines(qp)
            qp.end()

        def drawLines(self, qp):
            pen = QPen(Qt.black, 2, Qt.SolidLine)  # 初始配置

            qp.setPen(pen)
            qp.drawLine(20, 40, 250, 40)

            pen.setStyle(Qt.DashLine)  # 修改线条
            qp.setPen(pen)
            qp.drawLine(20, 80, 250, 80)

            pen.setStyle(Qt.DashDotLine)
            qp.setPen(pen)
            qp.drawLine(20, 120, 250, 120)

            pen.setStyle(Qt.DotLine)
            qp.setPen(pen)
            qp.drawLine(20, 160, 250, 160)

            pen.setStyle(Qt.DashDotDotLine)
            qp.setPen(pen)
            qp.drawLine(20, 200, 250, 200)

            pen.setStyle(Qt.CustomDashLine)
            pen.setDashPattern([1, 4, 5, 4])
            qp.setPen(pen)
            qp.drawLine(20, 240, 250, 240)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def brushes():
    """
    不同类型填充的长方形
    """
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QPainter, QBrush
    from PyQt5.QtCore import Qt

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 355, 280)
            self.setWindowTitle('Brushes')
            self.show()

        def paintEvent(self, e):
            qp = QPainter()
            qp.begin(self)
            self.drawBrushes(qp)
            qp.end()

        def drawBrushes(self, qp):
            brush = QBrush(Qt.SolidPattern)
            qp.setBrush(brush)
            qp.drawRect(10, 15, 90, 60)

            brush.setStyle(Qt.Dense1Pattern)
            qp.setBrush(brush)
            qp.drawRect(130, 15, 90, 60)

            brush.setStyle(Qt.Dense2Pattern)
            qp.setBrush(brush)
            qp.drawRect(250, 15, 90, 60)

            brush.setStyle(Qt.DiagCrossPattern)
            qp.setBrush(brush)
            qp.drawRect(10, 105, 90, 60)

            brush.setStyle(Qt.Dense5Pattern)
            qp.setBrush(brush)
            qp.drawRect(130, 105, 90, 60)

            brush.setStyle(Qt.Dense6Pattern)
            qp.setBrush(brush)
            qp.drawRect(250, 105, 90, 60)

            brush.setStyle(Qt.HorPattern)
            qp.setBrush(brush)
            qp.drawRect(10, 195, 90, 60)

            brush.setStyle(Qt.VerPattern)
            qp.setBrush(brush)
            qp.drawRect(130, 195, 90, 60)

            brush.setStyle(Qt.BDiagPattern)
            qp.setBrush(brush)
            qp.drawRect(250, 195, 90, 60)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


def bezier_curve():
    """
    贝塞尔曲线
    """
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QPainter, QPainterPath
    from PyQt5.QtCore import Qt

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 380, 250)
            self.setWindowTitle('Bézier curve')
            self.show()

        def paintEvent(self, e):
            qp = QPainter()
            qp.begin(self)
            qp.setRenderHint(QPainter.Antialiasing)
            self.drawBezierCurve(qp)  # 画曲线
            qp.end()

        def drawBezierCurve(self, qp):
            path = QPainterPath()
            path.moveTo(30, 30)
            path.cubicTo(30, 30, 200, 350, 350, 30) # 找点

            qp.drawPath(path)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# drawing_text()
# points()
# colours()
# pens()
# brushes()
bezier_curve()
