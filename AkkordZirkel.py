import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Rotator(QDialog):
    def __init__(self, graphicsItem):
        QDialog.__init__(self)
        self.graphicsItem = graphicsItem

    def eventFilter(self, receiver, event):
        if event.type() != QEvent.KeyPress:
            return super().eventFilter(receiver, event)

        key = QKeyEvent(event).key()

        if key == Qt.Key_Right:
            self.rotate(30)
        elif key == Qt.Key_Left:
            self.rotate(-30)
        elif key == Qt.Key_Q:
            QApplication.exit()
        else:
            return super().eventFilter(receiver, event)

        return True

    def rotate(self, angle):
        graphicsItem = self.graphicsItem
        graphicsItem.setRotation(graphicsItem.rotation() + angle)
        graphicsItem.update()

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()

    o_image = QImage("outer.png")
    outer = QGraphicsPixmapItem(QPixmap.fromImage(o_image))

    i_image = QImage("inner.png")
    inner = QGraphicsPixmapItem(QPixmap.fromImage(i_image))
    inner.setZValue(1)
    x = (o_image.width() - i_image.width()) / 2
    y = (o_image.height() - i_image.height()) / 2
    inner.setPos(x, y)
    inner.setTransformOriginPoint(i_image.width()/2, i_image.height()/2)

    rotator = Rotator(inner)
    window.installEventFilter(rotator)

    canvas = QGraphicsScene()
    canvas.addItem(inner)
    canvas.addItem(outer)

    view = QGraphicsView(canvas, window)
    view.resize(450, 450)

    window.resize(450, 450)
    window.grabKeyboard()

    window.setStyleSheet("background:transparent;")
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.setWindowFlags(Qt.FramelessWindowHint)

    window.show()

    app.exec_()

if __name__ == '__main__':
    main()
