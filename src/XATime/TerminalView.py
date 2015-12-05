#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from PyQt4.QtCore import QTimer, Qt, QSize
from PyQt4.QtGui import QDialog, QPicture, QIcon
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
        self.pbKommen.setIconSize(QSize(100, 100))
        self.pbKommen.setIcon(QIcon(":/icons/kommen.svg"))

        self.pbGehen.setIconSize(QSize(100, 100))
        self.pbGehen.setIcon(QIcon(":/icons/gehen.svg"))

        self.pbPause.setIconSize(QSize(50, 50))
        self.pbPause.setIcon(QIcon(":/icons/pause.svg"))

        self.pbStatus.setIconSize(QSize(50, 50))
        self.pbStatus.setIcon(QIcon(":/icons/status.svg"))


        # self.showFullScreen()
        # self.setCursor(Qt.BlankCursor)
        self.resize(800, 480)

        # icon = QIcon("icons_log.svg")
        # pixmap = icon.pixmap(24, 24)
        # print icon
        # self.labelStatus.setPixmap(pixmap)
        # self.pbKommen.setIcon(icon)

    def setupTimer(self):
        self.clockTimer = QTimer()
        self.clockTimer.setInterval(1000)
        self.clockTimer.timeout.connect(self.slotClockTimerTimeOut)
        self.clockTimer.start()

    def slotClockTimerTimeOut(self):
        self.labelClock.setText("{dt:%d.%m.%Y   %H:%M}".format(dt=datetime.datetime.now()))

    def setMode(self, mode):
        self.mode = mode
        self.labelMiddleLower.setText(self.modeTexts[mode])