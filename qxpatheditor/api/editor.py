"""
This module contains the editor widget implementation.
"""
from qxpatheditor.qt import QtCore, QtGui, QtWidgets
from .forms import editor_ui
from .match_highlighter import MatchHighlighter
from lxml import html


class XPathEditorWidget(QtWidgets.QWidget):
    try:
        quick_ref_requested = QtCore.Signal(int)
    except AttributeError:
        quick_ref_requested = QtCore.pyqtSignal(int)

    @property
    def string(self):
        """
        Gets/Sets the test string
        """
        return self.ui.plainTextEditTestString.toPlainText()

    @string.setter
    def string(self, value):
        self.ui.plainTextEditTestString.setPlainText(value)

    @property
    def xpath(self):
        """
        Gets/Sets the regular expression
        :return:
        """
        return self.ui.lineEditXPath.text()

    @xpath.setter
    def xpath(self, value):
        self.ui.lineEditXPath.setText(value)

    @property
    def quick_ref_checked(self):
        """
        Gets/sets the show quick ref checkbox state
        """
        return self.ui.checkBoxQuickRef.isChecked()

    @quick_ref_checked.setter
    def quick_ref_checked(self, value):
        self.ui.checkBoxQuickRef.setChecked(value)

    def __init__(self, parent=None):
        super(XPathEditorWidget, self).__init__(parent)
        self.ui = editor_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lblError.hide()

        self.ui.lineEditXPath.textChanged.connect(self._update_view)
        self.ui.plainTextEditTestString.textChanged.connect(
            self._update_view)
        doc = self.ui.plainTextEditMatchResult.document()
        self._highlighter = MatchHighlighter(doc)
        self._highlighter.rehighlight()
        self.ui.checkBoxQuickRef.stateChanged.connect(
            self.quick_ref_requested)
        self.ui.checkBoxIgnoreCase.stateChanged.connect(self._update_view)

    @staticmethod
    def _set_widget_background_color(widget, color):
        """
        Changes the base color of a widget (background).
        :param widget: widget to modify
        :param color: the color to apply
        """
        pal = widget.palette()
        pal.setColor(pal.Base, color)
        widget.setPalette(pal)

    def _show_error(self, error):
        self.ui.lblError.show()
        self.ui.lblError.setText('Error: %s' % error)
        self._set_widget_background_color(
            self.ui.lineEditXPath, QtGui.QColor('#fcbbbb'))
        self._highlighter.prog = None
        self._highlighter.rehighlight()

    def _show_match_results(self, prog, isChecked):
        self.ui.lblError.hide()
        self._set_widget_background_color(
            self.ui.lineEditXPath, QtGui.QColor('#bbfcbb'))
        if isChecked is True:
            if len(prog) > 0:
                matches = ""
                for x in prog:
                    matches += str(x) + "\n"
                self.ui.plainTextEditMatchResult.setPlainText(
                    str(matches))
        elif isChecked is False:
            self.ui.plainTextEditMatchResult.setPlainText(
                self.ui.plainTextEditTestString.toPlainText())
            self._highlighter.prog = prog
            self._highlighter.rehighlight()
        

    def _clear(self):
        self.ui.lblError.hide()
        pal = self.palette()
        self._set_widget_background_color(
            self.ui.lineEditXPath, pal.color(pal.Base))
        self._highlighter.prog = None
        self._highlighter.rehighlight()

    def _update_view(self, *args):
        if self.xpath:
            try:
                doc = self.ui.plainTextEditTestString.toPlainText()
                prog = html.fromstring(doc).xpath(str(self.xpath))
            except Exception as e:
                self._show_error(e)
            else:
                self._show_match_results(prog, self.ui.checkBoxIgnoreCase.isChecked())
        else:
            self._clear()
