#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import QApplication

from XATime.TerminalView import TerminalView

__author__ = 'Marco Bartel'


class xatime_terminal(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tv = TerminalView()
        self.tv.show()
        self.app.exec_()

    def loadCss(self):
        scss = Scss()
        scss_data = open("xatime_terminal.scss")
        css = scss.compile(scss_data)
        print css


if __name__ == '__main__':
    xtt = xatime_terminal()
