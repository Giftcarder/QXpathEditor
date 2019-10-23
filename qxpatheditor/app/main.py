"""
Application entry point
"""
import sys
from qxpatheditor.qt import QtWidgets
from qxpatheditor.app.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
