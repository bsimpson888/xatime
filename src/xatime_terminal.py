#!/usr/bin/env python
# -*- coding: utf-8 -*-
import locale
import os
import sys

from PyQt4.QtGui import QApplication
from scss import Scss

from XATime.SimpleDaemon import SimpleDaemon
from XATime.TerminalView import TerminalView

__author__ = 'Marco Bartel'


class xatime_terminal(object):
    def __init__(self):
        SimpleDaemon.debug = True
        logPath = "/home/pi/xatime/logs" if SimpleDaemon.windows else "c:\\temp\\xatime\\logs"

        with SimpleDaemon("xatime_terminal", usePidFile=False, logPath=logPath) as daemon:
            print "starte xatime_terminal in", os.getcwd()


            if sys.platform in ("posix", "linux2"):
                os.environ["DISPLAY"] = ":0.0"
                locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
            else:
                locale.setlocale(locale.LC_ALL, 'deu_deu')

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
