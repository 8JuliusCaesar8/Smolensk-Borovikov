import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PIL import Image

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Диалоговые окна')
        self.b1 = QPushButton('R', self)
        self.b1.resize(100, 50)
        self.b1.move(50, 100)
        self.b2 = QPushButton('G', self)
        self.b2.resize(100, 50)
        self.b2.move(50, 200)
        self.b3 = QPushButton('B', self)
        self.b3.resize(100, 50)
        self.b3.move(50, 300)
        self.b4 = QPushButton('ALL', self)
        self.b4.resize(100, 50)
        self.b4.move(50, 400)
        self.b_c = QPushButton('По часовой стрелке', self)
        self.b_c.resize(200, 50)
        self.b_c.move(250, 350)
        self.b_p = QPushButton('Против часовой стрелки', self)
        self.b_p.resize(200, 50)
        self.b_p.move(250, 400)

        self.pixmap = QPixmap('img.png')
        self.image = QLabel(self)
        self.image.move(200, 100)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

        im = Image.open("img.png")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = g, b, r

    def r(self):
        im = Image.open("img.png")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = g, b, r
        im.save('img1.png')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())