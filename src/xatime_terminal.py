#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import QApplication
from scss import Scss

from XATime.TerminalView import TerminalView

__author__ = 'Marco Bartel'


class xatime_terminal(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tv = TerminalView()
        self.tv.show()
        self.app.setStyleSheet(self.loadCss())
        self.app.exec_()

    def loadCss(self):
        scss = Scss()
        scss_data = open("xatime_terminal.scss", "rb").read()
        css = scss.compile(scss_data)
        return css


if __name__ == '__main__':
    xtt = xatime_terminal()
