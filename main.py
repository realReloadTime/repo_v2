import sys
from random import randint

from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class RandomCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btn = self.pushButton
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp.begin(self)
            self.draw_circle(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        self.qp.setPen(QColor(0, 0, 0))
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        side = randint(5, 200)
        self.qp.drawEllipse(randint(1, 273), randint(1, 100), side, side)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircles()
    ex.show()
    sys.exit(app.exec())
