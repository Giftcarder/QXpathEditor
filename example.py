"""
This example show you how to use the widget in a custom application.
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# if you use PyQt4 or PySide, you must set the QT_API environment variable
# to select the proper bindings, see
# https://github.com/pyQode/pyQode/wiki/Getting-started#qt-bindings-selection
from qxpatheditor.api import XPathEditorWidget, QuickRefWidget

try:
    app = QApplication(sys.argv)
    window = QMainWindow()
    editor = XPathEditorWidget()
    quick_ref = QuickRefWidget()
    quick_ref.hide()
    window.setCentralWidget(editor)
    # show/hide quick reference widget
    editor.quick_ref_requested.connect(quick_ref.setVisible)
    window.show()
    app.exec_()
except Exception as e:
    print(e)
