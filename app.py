import sys

from PyQt4 import QtCore, QtGui, uic


class MyWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = uic.loadUi("app.ui")

        self.connect(self.ui.car_button, QtCore.SIGNAL("clicked()"), self.add_car)

        self.ui.show()


        self.count = 0

    def add_car(self):
        self.count += 1
        self.ui.car_count.setText(str(self.count))
        print self.ui.palaute.toPlainText()


app = QtGui.QApplication(sys.argv)
window = MyWindow()
app.exec_()
