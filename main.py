import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from calculator import *


class Calculator(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.calculator = Ui_Form()
        self.calculator.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
