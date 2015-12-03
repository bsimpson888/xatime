#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QDialog

from XATime.ui.Ui_TerminalView import Ui_TerminalView

__author__ = 'Marco Bartel'


class TerminalView(QDialog, Ui_TerminalView):

    MODUS_KOMMEN, MODUS_GEHEN, MODUS_PAUSE, MODUS_STATUS = range(4)

    modeTexts = {
        MODUS_KOMMEN: "Kommen",
        MODUS_GEHEN: "Gehen",
        MODUS_PAUSE: "Pause",
        MODUS_STATUS: "Status"
    }

    def __init__(self, parent=None):
        super(TerminalView, self).__init__(parent)
        self.setupUi(self)
        self.setupWidgets()
        self.setupTimer()
        self.setMode(self.MODUS_KOMMEN)

    def setupWidgets(self):
        self.resize(800, 480)

    def setupTimer(self):
        self.clockTimer = QTimer()
        self.clockTimer.setInterval(1000)
        self.clockTimer.timeout.connect(self.slotClockTimerTimeOut)
        self.clockTimer.start()

    def slotClockTimerTimeOut(self):
        self.labelClock.setText("{dt:%d.%m.%Y   %H:%M}".format(dt=datetime.datetime.now()))

    def setMode(self, mode):
        self.mode = mode
        self.labelMode.setText(self.modeTexts[mode])