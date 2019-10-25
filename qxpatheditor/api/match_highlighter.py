from qxpatheditor.qt import QtGui


class MatchHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        super(MatchHighlighter, self).__init__(document)
        self.prog = None
        self._format = QtGui.QTextCharFormat()
        self._format.setBackground(QtGui.QBrush(QtGui.QColor('#0051ff')))

    def highlightBlock(self, text):
        if self.prog and text:
            if len(self.prog) > 0:
                value = self.prog[0]
                find = text.find(str(value))
                start, end = (find, find+len(str(value)))
                self.setFormat(start, end - start, self._format)
